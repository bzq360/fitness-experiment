import pandas as pd


def compute_average():
    df = pd.read_csv("analysis.csv")
    df = df.groupby(['problem name', 'fitness type'], as_index=False) \
        .agg({'number of fixed patch': ['mean'],
              'number of better patches': ['mean'],
              'portion of better patches': ['mean'],
              'number of equal patches': ['mean'],
              'portion of equal patches': ['mean']})
    df.columns = df.columns.droplevel(level=0)
    df.columns = ['problem', 'fitness type', '# fixed patches mean', '# better patches mean', '% better patches mean', '# same patches mean', '% same patches mean']
    # float to percentage
    df['% better patches mean'] = df['% better patches mean'].astype(float).map("{:.2%}".format)
    df['% same patches mean'] = df['% same patches mean'].astype(float).map("{:.2%}".format)
    df.to_csv('average.csv', encoding='utf-8', index=False)
    print('average computed')


if __name__ == '__main__':
    compute_average()
