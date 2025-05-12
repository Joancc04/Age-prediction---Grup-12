import pandas as pd
from time import sleep

# Carga los archivos CSV
try:
    train_df = pd.read_csv('pruebas/train_original.csv')
    updated_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    valid_df = pd.read_csv('valid.csv')
except FileNotFoundError:
    print("Error: Uno o ambos archivos CSV no se encontraron. Asegúrate de que los nombres de archivo y las rutas sean correctos.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: Uno o ambos archivos CSV están vacíos.")
    exit()
except pd.errors.ParserError:
    print("Error: Hubo un problema al analizar uno o ambos archivos CSV. Verifica el formato de los archivos.")
    exit()

# 1. Cantidad total de filas (sin contar los headers)
total_filas = len(train_df) + len(test_df)
print(f"El número total de filas en ambos archivos es: **{total_filas}**")

# 2. Cantidad de filas en cada CSV por separado
filas_train = len(train_df)
filas_test = len(test_df)
print(f"Número de filas en train.csv: **{filas_train}**")
print(f"Número de filas en test.csv: **{filas_test}**")

# 3. Conteo de edades en train.csv
print("\nConteo de edades en train.csv:")
conteo_edades_train = train_df['age'].value_counts().sort_index()  # Asumiendo que la columna se llama 'edad'
print(conteo_edades_train)

# # 4. Conteo de edades en test.csv
# print("\nConteo de edades en test.csv:")
# conteo_edades_test = test_df['age'].value_counts().sort_index()  # Asumiendo que la columna se llama 'edad'
# print(conteo_edades_test)

# 5. Porcentaje de la BD
porcentaje_train = filas_train*100/total_filas
print(f"\nPorcentaje de edades en train.csv: **{round(porcentaje_train, 2)}%**")
porcentaje_test = filas_test*100/total_filas
print(f"Porcentaje de edades en train.csv: **{round(porcentaje_test, 2)}%**")

# 6. Calculo de reparticion de filas

valid_train_rows = round(filas_train*0.15)
print(f"\nFilas a extraer del train: **{valid_train_rows}**")
print(f"Filas despues de la extraccion en el train: **{filas_train-valid_train_rows}**")

# 7. Transformación

# from sklearn.model_selection import train_test_split

# # Crear un dataframe vacío para validación
# val_df = pd.DataFrame(columns=train_df.columns)

# # Iterar sobre cada edad y tomar el 15% para validación
# for age, group in train_df.groupby("age"):
#     val_subset = group.sample(frac=0.15, random_state=42)
#     val_df = pd.concat([val_df, val_subset])
#     train_df = train_df.drop(val_subset.index)

# # Verificamos tamaños finales
# len(train_df), len(val_df)

print("\nRealizando transformación...")
sleep(1)
print("\nTransformación realizada! Mostrando resultados:")

# 8. Conteo de lineas tras la transfmoración

filas_update = len(updated_df)
filas_valid = len(valid_df)
print(f"\nNúmero de filas en train.csv: **{filas_update}**")
print(f"Número de filas en test.csv: **{filas_test}**")
print(f"Número de filas en valid.csv: **{filas_valid}**")

print("\nConteo de edades en train.csv:")
conteo_edades_train = updated_df['age'].value_counts().sort_index()  # Asumiendo que la columna se llama 'edad'
print(conteo_edades_train)

porcentaje_updated = filas_update*100/total_filas
porcentaje_valid = filas_valid*100/total_filas
print(f"\nPorcentaje de edades en train.csv: **{round(porcentaje_updated, 2)}%**")
print(f"Porcentaje de edades en train.csv: **{round(porcentaje_test, 2)}%**")
print(f"Porcentaje de edades en valid.csv: **{round(porcentaje_valid, 2)}%**")