import os
import pandas as pd
import re


main_df = pd.DataFrame(
    columns=['fitness type', 'problem name', 'mutation seed', 'selection seed', 'number of fixed patch',
             'number of evaluations to find first fixed patch', 'number of better patches', 'portion of better patches',
             'number of equal patches', 'portion of equal patches'])


# analyze all files in results folder
def analyze_all():
    os.chdir(os.getcwd() + '/results')
    f_names = os.listdir()
    for f_name in f_names:
        print('analyzing ' + f_name)
        analyze_file(f_name)


# analyze file with input file name
def analyze_file(f_name):
    global main_df

    # parse file name
    info = re.findall("(\w+)-(\w+)-(\d+)-(\d+).csv", f_name)[0]
    fitness = info[0]
    problem = info[1]
    m_seed = info[2]
    s_seed = info[3]

    # read file content
    df = pd.read_csv(f_name)
    init_fit_value = df.iloc[0]['Fitness']
    num_patch = len(df)

    # number of fixed patch
    fix_df = df[df['AllTestsPassed']]  # TODO: output fixed patch to another file
    num_fix = len(fix_df)

    # number of evaluations to find the first fix; -1 if no fix is found
    if num_fix == 0:
        first_fix = -1
    else:
        first_fix = fix_df.index.values[0]

    # number/percentage of better fitness patches
    better_df = df[df['Fitness'] < init_fit_value]
    num_better = len(better_df)
    portion_better = num_better / num_patch

    # number/percentage of same fitness patches
    same_df = df[df['Fitness'] == init_fit_value]
    num_same = len(same_df)
    portion_same = num_same / num_patch

    # save on main df
    save_df = pd.Series(
        [fitness, problem, m_seed, s_seed, num_fix, first_fix, num_better, portion_better, num_same, portion_same],
        index=main_df.columns)
    # print(save_df)
    main_df = main_df.append(save_df, ignore_index=True)


# main function
if __name__ == '__main__':
    path = os.getcwd()
    analyze_all()
    os.chdir(path)
    main_df.to_csv('analysis.csv', encoding='utf-8', index=False)
