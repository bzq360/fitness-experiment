import random

# disable patch analyzer for fixed patches found
disable_patch_analyzer = True

# run with evosuite generated test cases
contain_evosuite = [False, True]

# gin project absolute path
gin_dir = 'C:\\UCL\\IdeaProjects\\gin'

# number of maximum generations
max_generations = 20

# population size
population_size = 100

# random seeds [mutation, mutant selection]
seeds = [
    (111, 111),
    (753, 753),
    (1024, 1024),
    # (666, 666)
]

# fully random on seeds (overwrite above seeds)
num_run = 3

# maximum time on running a test case
timeout = 2000

# supported edit types
edits = [
    'STATEMENT',
    # 'MATCHED_STATEMENT',
    # 'MODIFY_STATEMENT',
    # 'INSERT_STATEMENT',
    # 'LINE'
]

# fitness function types
fitness_types = [
    'original',
    'decision',
    'arjae',
    # 'checkpoint' # not supported
]

# benchmark problems (15 in total)
problems = [
    # 'depth_first_search',
    # # 'detect_cycle', # slow
    # 'find_in_sorted',
    # 'get_factors',
    # # 'hanoi',  # not supported
    # 'is_valid_parenthesization',
    # # 'knapsack', # slow
    'levenshtein',
    # 'lis',
    # 'mergesort',
    # # 'overflow', # slow
    # 'next_permutation',
    # 'powerset',
    # # 'quicksort', # slow
    # 'rpn_eval', # too many fixed patches
    # 'shortest_path_lengths' # not supported
]


def create_seed():
    global seeds
    if num_run > 0:
        seeds = []
        for i in range(num_run):
            seeds.append((random.randint(1, 1000000), random.randint(1, 1000000)))
    return seeds


if __name__ == '__main__':
    create_seed()
