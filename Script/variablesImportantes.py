import pandas as pd
import joblib


nombre_archivo = 'modelo_ff_rf.pkl'
modelo_rf = joblib.load(nombre_archivo)

df_train = pd.read_csv('entrenamiento_lol.csv')
X_train = df_train.drop(columns=['blueWins', 'gameId'])

importancias = modelo_rf.feature_importances_
nombres_variables = X_train.columns

df_importancias = pd.DataFrame({
    'variable': nombres_variables,
    'importancia': importancias 
})

df_importancias = df_importancias.sort_values(by='importancia', ascending=False)

print("10 variables mas importantes:")
print(df_importancias.head(10).to_string(index=False))