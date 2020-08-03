import pandas as pd


def compute_average():
    df = pd.read_csv("analysis.csv")
    df = df.groupby(['problem name', 'fitness type', 'evosuite'], as_index=False) \
        .agg({'number of fixed patch': ['mean'],
              'number of evaluations to find first fixed patch': ['min'],
              'number of better patches': ['mean'],
              'ratio of better patches': ['mean'],
              'number of equal patches': ['mean'],
              'ratio of equal patches': ['mean']})
    df.columns = df.columns.droplevel(level=0)
    df.columns = ['problem', 'fitness type', 'evosuite', 'number of fixed patches found', 'number of evaluations to find first fixed patch', 'number of better fitness patches', 'ratio of better fitness patches', 'number of same fitness patches', 'ratio of same fitness patches']
    # float to percentage
    df['ratio of better fitness patches'] = df['ratio of better fitness patches'].astype(float).map("{:.2%}".format)
    df['ratio of same fitness patches'] = df['ratio of same fitness patches'].astype(float).map("{:.2%}".format)
    df['number of fixed patches found'] = df['number of fixed patches found'].map('{:.2f}'.format)
    df['number of better fitness patches'] = df['number of better fitness patches'].map('{:.2f}'.format)
    df['number of same fitness patches'] = df['number of same fitness patches'].map('{:.2f}'.format)
    df.to_csv('average.csv', encoding='utf-8', index=False)
    print('average computed')


if __name__ == '__main__':
    compute_average()
