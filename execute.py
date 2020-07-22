import os

# gin project absolute path
gin_dir = 'C:\\UCL\\IdeaProjects\\gin'

# number of maximum generations
max_generations = 3

# population size
population_size = 1

# random seeds [mutation, mutant selection]
seeds = [
    (123, 123),
    (777, 777),
]

# supported edit types
edits = [
    'STATEMENT',
    'MATCHED_STATEMENT',
    'MODIFY_STATEMENT',
    # 'INSERT_STATEMENT',
    # 'LINE'
]

# fitness function types
fitness_types = [
    'original',
    'decision',
    # 'arjae',
    # 'checkpoint'
]

# benchmark problems
problems = [
    # 'depth_first_search',
    # 'detect_cycle',
    # 'find_in_sorted',
    # 'get_factors',
    # 'hanoi',
    # 'is_valid_parenthesization',
    # 'knapsack',
    # 'levenshtein',
    'lis',
    # 'mergesort',
    # 'overflow',
    # 'next_permutation',
    # 'powerset',
    'quicksort',
    # 'rpn_eval',
    # 'shortest_path_lengths'
]


# construct command line for GIN
def get_all_fix_command():
    commands = []
    for type in fitness_types:
        for problem in problems:
            for seed in seeds:
                commands.append(get_fix_command(type, problem, seed[0], seed[1]))
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
        java_class = 'gin.util.GPNovel'
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
    command += '-o ' + 'results/' + fitness_type + '-' + problem + '-' + str(mutation_seed) + '-' + str(selection_seed) + '.csv '
    command += '-et '
    for edit in edits:
        command += edit + ','
    command = command[:-1]
    command += ' '
    command += '-ms ' + str(mutation_seed) + ' -is ' + str(selection_seed)
    return command


def exec_all_fix():
    os.chdir(gin_dir)  # navigate to gin directory
    for command in get_all_fix_command():
        os.system(command)


def analyze():
    os.chdir(gin_dir + '\\results')
    # print(os.listdir())

# main function
if __name__ == '__main__':
    output_all_fix_command()
    # print(os.listdir())
