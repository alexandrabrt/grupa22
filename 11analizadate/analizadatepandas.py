import pandas as pd
import numpy as np
import datetime

# din lista
# lista = [10, 20, 30, 40, 50]
# serie = pd.Series(lista)
# print(serie)

# din array NumPy
# array_date = np.array([10, 20, 30, 40, 50])
# print(array_date)
# print(type(array_date))
# serie = pd.Series(array_date)
# print(serie)

# din dictionar
# dict_date = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# serie = pd.Series(dict_date)
# print(serie)


# adaugare eticheta lista
# date = [10, 20, 30, 40, 50]
# etichete = ['a', 'b', 'c', 'd', 'e']
# serie = pd.Series(date, index=etichete)
# print(serie['b'])
# print(serie[['a', 'c', 'e']])
# print(serie['b': 'd'])
# print(serie[1: 4])
# print(serie[serie > 30])

# date_si_timp = [datetime.datetime(2022, 1, 1),
#                 datetime.datetime(2022, 1, 2),
#                 datetime.datetime(2022, 1, 3)]
# ser_temporala = pd.Series([10, 20, 30], index=date_si_timp)
# # print(ser_temporala['2022-01-02'])
# print(ser_temporala['2022-01-01': '2022-01-02'])

# data = {'Nume': ['Ana', 'Bogdan', 'Cristina'],
#         'Varsta': [25, 30, 22],
#         'Salariu': [50000, 60000, 45000]}
# df = pd.DataFrame(data)
# df['Experienta'] = [2, 5, 1]
# df_sortat = df.sort_values(by='Varsta', ascending=True)
# print(df_sortat)
# df_sortat_index = df.sort_index()
# print(df_sortat_index)
# df_filtrat = df[df['Varsta'] > 25]
# df_filtrat = df[(df['Varsta'] > 22) & (df['Experienta'] >= 2)]
# print(df_filtrat)
# df.set_index('Nume', inplace=True)
# df.reset_index(inplace=True)
# print(df)
# print(df.loc['Bogdan'])
# print(df.iloc[1])
# print(df.loc[['Ana', 'Cristina'], ['Varsta', 'Salariu']])
# nume = df['Nume']
# print(nume)
# salariu_bogdan = df.at[1, 'Salariu']
# varsta_cristina = df.at[2, 'Varsta']
# print(varsta_cristina)


# data = {'Nume': ['Ana', 'Bogdan', 'Ana', 'Cristina', 'David', 'Ana'],
#         'Varsta': [25, 30, 25, 22, 35, 25],
#         'Salariu': [50000, 60000, 50001, 45000, 70000, 50000]}
# df = pd.DataFrame(data)
# print(df)
# df.drop_duplicates(subset=['Nume', 'Varsta'], inplace=True)
# print(df)

# data = {'Nume': ['Ana', 'Bogdan', None, 'Cristina', 'David'],
#         'Varsta': [25, 30, None, 22, 35],
#         'Salariu': [50000, None, 45000, 70000, 60000]}
# df = pd.DataFrame(data)
# df.loc[[0, 2], 'Experienta'] = 100
# # df.dropna(inplace=True)
# # df['Salariu'].fillna(0, inplace=True)
# # df['Varsta'].fillna(0, inplace=True)
# # df.fillna({'Varsta': 0, 'Salariu': 0}, inplace=True)
# df['Experienta'] = [2, 5, 1, 4, 3]
# df.rename(columns={'Nume': 'Nume_nou', "Varsta": 'Varste', 'Salariu': 'Salariul'}, inplace=True)
# print(df)


# data = {'Nume': ['Ana', 'Bogdan', 'Cristina', 'David', 'Elena', 'Florin'],
#         'Varsta': [25, 30, 22, 35, 28, 40],
#         'Salariu': [50000, 60000, 45000, 70000, 55000, 80000],
#         'Departament': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR']}

# df = pd.DataFrame(data)
# grupuri_departamente = df.groupby('Departament')
# for nume_departament, grup in grupuri_departamente:
#         print(f"\nGrupul pentru departament: {nume_departament} ")
#         print(grup)
# medie_salarii = grupuri_departamente['Salariu'].mean()
# print('\nMedia salariilor pentru fiecare departament:')
# print(medie_salarii)
# rezultate_agregare = grupuri_departamente.agg({'Varsta': 'mean', 'Salariu': ['sum', 'median'], 'Nume': 'count'})
# print(rezultate_agregare)
# print(df)

# data = {'Data': ['2022-01-01', '2022-01-02', '2022-01-03'],
#         'Vanzari': [100, 150, 200]}
# df = pd.DataFrame(data)
# # print(df.dtypes)
#
# df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d', errors='coerce')
# df['Data'] = df['Data'].dt.strftime('%d-%m-%Y')
# df['Data'] = pd.to_datetime(df['Data'])
# # print(df.dtypes)
# df['Zi'] = df['Data'].dt.day
# df['Luna'] = df['Data'].dt.month
# df['An'] = df['Data'].dt.year
# # print(df)
# df['Diferenta_zi'] = (df['Data'] - pd.to_datetime('2022-01-01')).dt.days
# print(df)

# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Nume': ['Cristina', 'David'], 'Varsta': [22, 35]})
#
# df_concat_randuri = pd.concat([df1, df2], ignore_index=True)
# print(df_concat_randuri)
#
# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Salariu': [50000, 60000], 'Experienta': [2, 5]})
#
# df_concatenat = pd.concat([df1, df2], axis=1)
# print(df_concatenat)
#
# # df_concatenat.to_csv('nou.csv', index=False)
# df_concatenat.to_csv('nou.csv')
