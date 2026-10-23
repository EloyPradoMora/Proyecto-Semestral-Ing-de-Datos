import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df_train = pd.read_csv('entrenamiento_lol.csv')
X_train = df_train.drop(columns=['blueWins', 'gameId'])
y_train = df_train['blueWins']

modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
print("Entrenando el modelo con Random Forest, espere...")

modelo_rf.fit(X_train, y_train)

nombre_archivo = 'modelo_ff_rf.pkl'
joblib.dump(modelo_rf, nombre_archivo)

print(f"Listo el modelo fue fuardado como '{nombre_archivo}'")