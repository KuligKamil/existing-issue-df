import pandas as pd
import numpy as np

# data frane need to be only with years and data
df = pd.DataFrame(data={'2021': pd.Series(['A']), '2020': pd.Series(['A', 'B']), '2019': pd.Series(['A', 'B', 'C']),
                        '2018': pd.Series(['A', 'B', 'C', 'D'])}, index=[0, 1, 2, 3, 4])
years = df.columns
df['existing'] = np.nan

iteration = 0
for index, values in df.iterrows():
    print()
    print('index', index)
    for value in values[:-1]:
        iteration += 1
        print('value', value)
        if value is not np.nan:
            df.loc[index, 'existing'] = value
            break
print()
print('iteration number: ', iteration)
