import os
import shutil
import pandas as pd
import re
from config import disable_patch_analyzer
from config import gin_dir
from config import pn_logging_level
from config import generations
from config import population_size
from config import output_logs_if_checkpoint

# current directory, don't touch, will be set in runtime
src = ''

main_df = pd.DataFrame(
    columns=['fitness type', 'problem name', 'evosuite', 'mutation seed', 'selection seed', 'number of fixed patch',
             'number of evaluations to find first fixed patch', 'number of better patches', 'ratio of better patches',
             'number of equal patches', 'ratio of equal patches'])


# analyze all files in results folder
def analyze_all():
    # clean fixed patch folder
    path = src + '/fixed_patches'
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    # analyze each result patch file
    os.chdir(src + '/results')
    f_names = os.listdir()
    for f_name in f_names:
        print('analyzing ' + f_name)
        analyze_file(src + '/results/' + f_name)


# analyze file with input file name
def analyze_file(f_name):
    global main_df

    # parse file name
    info = re.findall("(\w+)-(\w+)-(\d+)-(\d+)-(\w+).csv", f_name)[0]
    fitness = info[0]
    problem = info[1]
    m_seed = info[2]
    s_seed = info[3]
    evosuite = info[4]
    con_evo = (evosuite == 'e')

    # read file content
    df = pd.read_csv(f_name)
    init_fit_value = df.iloc[0]['Fitness']
    num_patch = len(df)

    # number of fixed patch
    fix_df = df[df['AllTestsPassed']]
    num_fix = len(fix_df)

    # number of evaluations to find the first fix; -1 if no fix is found
    if num_fix == 0:
        first_fix = generations * population_size + 1
    else:
        first_fix = fix_df.index.values[0]
        if not disable_patch_analyzer:
            # execute PatchAnalyser to get fixed patch
            os.chdir(gin_dir)
            cmd_prefix = 'java -Dtinylog.level=' + pn_logging_level[0]
            cmd_prefix += ' -cp build/gin.jar gin.PatchAnalyser ' + '-f quixbugs/faulty_programs/' + problem.upper() + '.java -p '
            fix = 1
            for patch in fix_df['Patch']:
                cmd = cmd_prefix + "\"" + patch + "\""
                os.system(cmd)
                shutil.move(gin_dir + '/quixbugs/faulty_programs/' + problem.upper() + '.java.patched',
                            src + '/fixed_patches')
                new_fn = src + '/fixed_patches/' + problem + '_' + fitness + '_' + m_seed + '_' + s_seed + '_' + evosuite + '_' + str(
                    fix) + '.txt'
                info_name = src + '/fixed_patches/' + problem + '_' + fitness + '_' + m_seed + '_' + s_seed + '_' + evosuite + '_' + str(
                    fix) + '_info.txt'
                os.rename(src + '/fixed_patches/' + problem.upper() + '.java.patched', new_fn)
                f = open(info_name, 'w')
                f.write(patch)
                fix += 1

    # number/percentage of better fitness patches
    better_df = df[df['Fitness'] > init_fit_value]
    num_better = len(better_df)
    portion_better = num_better / num_patch

    # number/percentage of same fitness patches
    same_df = df[df['Fitness'] == init_fit_value]
    num_same = len(same_df)
    portion_same = num_same / num_patch

    # save on main df
    save_df = pd.Series(
        [fitness, problem, con_evo, m_seed, s_seed, num_fix, first_fix, num_better, portion_better, num_same,
         portion_same],
        index=main_df.columns)

    main_df = main_df.append(save_df, ignore_index=True)


def analyze():
    global src
    src = os.getcwd()
    analyze_all()
    os.chdir(src)
    main_df.to_csv('analysis.csv', encoding='utf-8', index=False)


# main function
if __name__ == '__main__':
    analyze()
