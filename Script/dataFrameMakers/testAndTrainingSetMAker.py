import pandas as pd
from sklearn.model_selection import train_test_split

print("Creador de sets de entrenamiento corriendo...")
df = pd.read_csv('high_diamond_ranked_10min/high_diamond_ranked_10min.csv')

#el 80% de las filas deberan de estar en el dataset de entramiento mientras el 20% restante sera usado para el testeo
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['blueWins'])

df_train.to_csv('entrenamiento_lol.csv', index=False)
df_test.to_csv('testeo_lol.csv', index=False)

print("Archivos generados correctamente:")
print(f"- entrenamiento_lol.csv: {len(df_train)} filas")
print(f"- testeo_lol.csv: {len(df_test)} filas")