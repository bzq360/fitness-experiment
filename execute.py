import os

from config import fitness_types
from config import problems
from config import seeds
from config import max_generations
from config import population_size
from config import edits
from config import gin_dir


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
            for seed in seeds:
                f.write(get_fix_command(type, problem, seed[0], seed[1]) + '\n')
    f.close()


# generate command line for one fix
def get_fix_command(fitness_type, problem, mutation_seed, selection_seed):
    java_class = ''
    if fitness_type == 'original':
        java_class = 'gin.util.GPFix'
    elif fitness_type == 'decision':
        java_class = 'gin.util.GPNovelFix'
    elif fitness_type == 'arjae':
        java_class = 'gin.util.arjae'
    elif fitness_type == 'checkpoint':
        java_class = 'gin.util.checkpoint'

    command = ''
    command += 'java -cp build/gin.jar '
    command += java_class + ' '
    command += '-d quixbugs -c quixbugs '
    command += '-gn ' + str(max_generations) + ' '
    command += '-in ' + str(population_size) + ' '
    command += '-m quixbugs/quixbugs_method_files/' + problem + '.csv '
    command += '-o ' + 'results/' + fitness_type + '-' + problem + '-' + str(mutation_seed) + '-' + str(
        selection_seed) + '.csv '
    command += '-et '
    for edit in edits:
        command += edit + ','
    command = command[:-1]
    command += ' '
    command += '-ms ' + str(mutation_seed) + ' -is ' + str(selection_seed)
    return command


def exec_all_fix():
    os.chdir(gin_dir)  # navigate to gin directory
    for command in collect_all_fix_command():
        os.system(command)


# main function
if __name__ == '__main__':
    exec_all_fix()
    # TODO: Copy all files into current folder
