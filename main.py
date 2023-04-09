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
print(new_df)