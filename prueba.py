import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datos/datos_entrenamiento_laboratorio1(train_data).csv')


df[['cantidad', 'sufijo']] = df['market_value'].replace({  '-': np.nan, "error": np.nan}, regex=True).str.extract(r'€?([\d\.]+)([mk]?)')
df['cantidad'] = df['cantidad'].astype(float)

# Convertir según sufijo
df['precio_miles'] = df.apply(
    lambda row: row['cantidad'] * 1000 if row['sufijo'] == 'm' else row['cantidad'],
    axis=1
)

print(df.head())

null_counts = df.isnull().sum()
print(null_counts)

char = '-'
char_counts = df.apply(lambda col: col.astype(str).str.count(char).sum())
print(char_counts)

df.to_csv('Datos/datos_con_nueva_columna.csv', index=False)