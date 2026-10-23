import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score

nombre_archivo = 'modelo_ff_rf.pkl'
modelo_rf = joblib.load(nombre_archivo)
print(f"Modelo '{nombre_archivo}' cargado")

df_test = pd.read_csv('testeo_lol.csv')
X_test = df_test.drop(columns=['blueWins', 'gameId'])
y_test = df_test['blueWins']

print("Prediciendo...")
predicciones = modelo_rf.predict(X_test)

accuracy = accuracy_score(y_test, predicciones)
precision = precision_score(y_test, predicciones)
recall = recall_score(y_test,predicciones)

print("################################")
print("Resultados:")
print(f"Acurracy o exactitud: {accuracy * 100:.2f}%")
print(f"Presicion: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")