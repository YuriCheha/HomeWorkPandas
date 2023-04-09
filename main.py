import pandas as pd
df = pd.read_csv(r'C:\Users\user\Downloads\DATA_Pandas.csv')
df_stats = df.describe()
df_stats = df_stats.transpose()
print(df.dtypes)
new_df = pd.DataFrame({
    'count': df_stats['count'],
    'mean': df_stats['mean'],
    'std': df_stats['std'],
    'min': df_stats['min'],
    '25%': df_stats['25%'],
    '50%': df_stats['50%'],
    '75%': df_stats['75%'],
    'max': df_stats['max']
})
new_df.to_json('new_dataframe.json', orient='table')

aver_val = df['Temperature (K)'].mean()
df['delta_T'] = abs(df['Temperature (K)'] - aver_val)
if df.isnull().values.any():
    print('Датафрейм содержит NaN значение')
else:
    print('Датафрейм не содержит NaN значение')
Tmax = df['Temperature (K)'].max()
delta_Tmin = df['delta_T'].min()
new_df = df[(df['delta_T'] <= Tmax/2) & (df['Temperature (K)'] >= delta_Tmin)]
new_df.to_csv('new_df.csv', index=False)

