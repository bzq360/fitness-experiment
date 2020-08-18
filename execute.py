import os
import shutil

from config import fitness_types
from config import problems
from config import create_seed
from config import generations
from config import population_size
from config import edits
from config import gin_dir
from config import timeout
from config import contain_evosuite
from config import gp_logging_level
from config import run_in_new_process
from config import run_in_sub_process
from config import record_patch

# current directory, don't touch, will be set in runtime
src = ''

seeds = []


# construct command line for GIN
def collect_all_fix_command():
    output_all_fix_command()
    f = open('commands.txt', 'r')
    lines = f.readlines()
    commands = []
    for line in lines:
        commands.append(line)
    return commands


def output_all_fix_command():
    f = open("commands.txt", "w")
    for type in fitness_types:
        for problem in problems:
            for evosuite in contain_evosuite:
                for seed in seeds:
                    f.write(get_fix_command(type, problem, seed[0], seed[1], evosuite) + '\n')
    f.close()


# generate command line for one fix
def get_fix_command(fitness_type, problem, mutation_seed, selection_seed, evosuite):
    path = os.getcwd()
    path += '/results/'
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    java_class = ''
    if fitness_type == 'original':
        java_class = 'gin.util.GPFix'
    elif fitness_type == 'decision':
        java_class = 'gin.util.GPNovelFix'
    elif fitness_type == 'arjae':
        java_class = 'gin.util.GPArjaEFix'
    elif fitness_type == 'checkpoint':
        java_class = 'gin.util.GPCheckpointFix'

    command = 'java '
    command += '-Dtinylog.level=' + gp_logging_level[0] + ' '
    command += '-cp build/gin.jar '
    command += java_class + ' '
    command += '-d quixbugs -c quixbugs '
    command += '-gn ' + str(generations) + ' '
    command += '-in ' + str(population_size) + ' '
    if evosuite:
        command += '-m quixbugs/quixbugs_method_files/' + problem + '-evosuite.csv '
        command += '-o ' + path + fitness_type + '-' + problem + '-' + str(mutation_seed) + '-' + str(
            selection_seed) + '-e.csv '
    else:
        command += '-m quixbugs/quixbugs_method_files/' + problem + '.csv '
        command += '-o ' + path + fitness_type + '-' + problem + '-' + str(mutation_seed) + '-' + str(
            selection_seed) + '-o.csv '
    command += '-et '
    for edit in edits:
        command += edit + ','
    command = command[:-1]
    command += ' '
    command += '-ms ' + str(mutation_seed) + ' -is ' + str(selection_seed) + ' '
    command += '-x ' + str(timeout) + ' '
    if record_patch:
        command += '-rec true '
    if run_in_new_process:
        command += '-j true '
    if run_in_sub_process:
        command += '-J true '
    if fitness_type == 'checkpoint':
        command += '-M quixbugs/quixbugs_method_files/' + problem + '_correct.csv'
    return command


def exec_all_fix():
    global src
    global seeds
    src = os.getcwd()
    seeds = create_seed()
    commands = collect_all_fix_command()
    os.chdir(gin_dir)  # navigate to gin directory
    for command in commands:
        print('process start: ' + command)
        os.system(command)
        print('process finish: ' + command)
    os.chdir(src)


# main function
if __name__ == '__main__':
    exec_all_fix()
