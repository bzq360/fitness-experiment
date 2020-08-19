import pandas as pd

from config import get_timestamp


def compute_average():
    # base directory
    base = 'output/{}'.format(get_timestamp())

    df = pd.read_csv("{}/analysis.csv".format(base))
    df = df.groupby(['problem name', 'fitness type', 'run with evosuite'], as_index=False) \
        .agg({'number of fixed patch': ['mean'],
              'number of fixed patch passed evosuite': ['mean'],
              'number of evaluations to find first fixed patch': ['min'],  # hard to measure as it can be meaningless
              'minimum number of edits to find a fix': ['min'],  # hard to measure as it can be meaningless
              'number of better patches': ['mean'],
              'ratio of better patches': ['mean'],
              'number of equal patches': ['mean'],
              'ratio of equal patches': ['mean']})
    df.columns = df.columns.droplevel(level=0)
    df.columns = ['problem', 'fitness type', 'run with evosuite', 'number of fixed patches found',
                  'number of fixed patch passed evosuite',
                  'number of evaluations to find first fixed patch', 'minimum number of edits to find a fix',
                  'number of better fitness patches', 'ratio of better fitness patches',
                  'number of same fitness patches', 'ratio of same fitness patches']
    # float to percentage
    df['ratio of better fitness patches'] = df['ratio of better fitness patches'].astype(float).map("{:.2%}".format)
    df['ratio of same fitness patches'] = df['ratio of same fitness patches'].astype(float).map("{:.2%}".format)
    df['number of fixed patches found'] = df['number of fixed patches found'].map('{:.2f}'.format)
    df['number of fixed patch passed evosuite'] = df['number of fixed patch passed evosuite'].map('{:.2f}'.format)
    df['number of better fitness patches'] = df['number of better fitness patches'].map('{:.2f}'.format)
    df['number of same fitness patches'] = df['number of same fitness patches'].map('{:.2f}'.format)
    df.to_csv('{}/average.csv'.format(base), encoding='utf-8', index=False)
    print('average.csv saved to {}'.format(base))


if __name__ == '__main__':
    compute_average()
