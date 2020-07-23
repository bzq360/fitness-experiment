# gin project absolute path
gin_dir = 'C:\\UCL\\IdeaProjects\\gin'

# number of maximum generations
max_generations = 1

# population size
population_size = 10

# random seeds [mutation, mutant selection]
seeds = [
    # (123, 123),
    (777, 777),
    # (1000, 1000),
    (666, 666)
]

# supported edit types
edits = [
    # 'STATEMENT',
    # 'MATCHED_STATEMENT',
    'MODIFY_STATEMENT',
    # 'INSERT_STATEMENT',
    # 'LINE'
]

# fitness function types
fitness_types = [
    'original',
    # 'decision',
    # 'arjae',
    # 'checkpoint'
]

# benchmark problems (15 in total)
problems = [
    # 'depth_first_search',
    # 'detect_cycle',
    # 'find_in_sorted',
    # 'get_factors',
    # 'hanoi',
    # 'is_valid_parenthesization',
    # 'knapsack',
    # 'levenshtein',
    # 'lis',
    # 'mergesort',
    # 'overflow',
    # 'next_permutation',
    # 'powerset',
    'quicksort',
    # 'rpn_eval',
    # 'shortest_path_lengths'
]
