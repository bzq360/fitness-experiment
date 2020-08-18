import random

# gp search logging level
gp_logging_level = [
    # 'trace',
    # 'debug',
    'info',
    # 'warning',
    # 'error'
]

# patch analyzer logging level
pn_logging_level = [
    # 'trace',
    # 'debug',
    # 'info',
    # 'warning',
    'error'
]

record_patch = True

run_in_new_process = False

run_in_sub_process = False

# disable patch analyzer for fixed patches found
# it will be slow on RPN_EVAL since there are too many identical patches
disable_patch_analyzer = False

# run with evosuite generated test cases
contain_evosuite = [
    False,
    True
]

# gin project absolute path
gin_dir = 'C:\\UCL\\IdeaProjects\\gin'

# number of maximum generations
generations = 10

# population size
population_size = 40

# random seeds [mutation, mutant selection]
seeds = [
    # (111, 111),
    # (753, 753),
    # (1024, 1024),
    # (666, 666)
]

# fully random on seeds (overwrite above seeds)
num_run = 1

# maximum time on running a test case
timeout = 1000

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
    # 'checkpoint' # only support LIS
]

# benchmark problems (17 in total, 2 have wrong method files)
# (problem name, )
problems = [
    # 'depth_first_search', # 79
    # 'detect_cycle',  # 350
    # 'find_in_sorted', # 117
    # 'get_factors', # 126
    # 'hanoi',  # wrong method file
    # 'is_valid_parenthesization', # 91
    # 'knapsack', # 417
    # 'levenshtein', # 183
    'lis', #69
    # 'mergesort', # 185
    # 'next_permutation', # 72
    # 'powerset', # 73
    # 'quicksort', # 2571 , found 50 identical fixes
    # 'rpn_eval', # 96, too many fixed patches
    # 'shortest_path_lengths' # wrong method file
    # 'sieve'
    # 'wrap' # slow
    ################ unrelated problems #################
    # 'bitcount',
    # 'to_base',
    # 'max_sublist_sum',
    # 'next_palindrome',
    # 'sqrt'
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
