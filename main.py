import pandas as pd
df = pd.read_csv(r'C:\Users\user\Downloads\DATA_Pandas.csv')
df_stats = df.describe()
df_stats = df_stats.transpose()
print(df.dtypes)
new_df1 = pd.DataFrame({
    'count': df_stats['count'],
    'mean': df_stats['mean'],
    'std': df_stats['std'],
    'min': df_stats['min'],
    '25%': df_stats['25%'],
    '50%': df_stats['50%'],
    '75%': df_stats['75%'],
    'max': df_stats['max']
})
new_df1.to_json('new_dataframe.json', orient='table')

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


corr_= df.corr(numeric_only = True)
mean_absolute_magnitude = df.groupby('Star type')['Absolute magnitude(Mv)'].mean()
count_by_spectral_class = df.groupby('Spectral Class').size()
sp_class_var = df.groupby('Star type')['Luminosity(L/Lo)'].var()
sem_ = df['Absolute magnitude(Mv)'].sem()
std_ = df['Temperature (K)'].std( )
new_df2 = pd.DataFrame({
    'mean_absolute_magnitude' : df.groupby('Star type')['Absolute magnitude(Mv)'].mean(),
    'count_by_spectral_class' : df.groupby('Spectral Class').size(),
    'sp_class_var': df.groupby('Star type')['Luminosity(L/Lo)'].var()
})
new_df2.to_xml('new_df2.xml')


df['temperature_C'] = df['Temperature (K)']  - 273.15
new_df = pd.DataFrame({
    'Temperature' : df['Temperature (K)'],
    'temperature_C' : df['temperature_C']
})
result_df1 = pd.concat([new_df1, new_df2], axis=1)
new_df2.join(new_df1)
if new_df2.isnull().values.any():
    print('Датафрейм содержит NaN значение')
else:
    print('Датафрейм не содержит NaN значение')
new_df2.interpolate()
test_data["A"] = new_df2['Temperature (K)'].fillna(test_data['Temperature (K)'].mean())
t = new_df2.dropna(axis=0)


