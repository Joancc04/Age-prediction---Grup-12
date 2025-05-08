import os
import csv
import shutil
from pathlib import Path

# Define rutas
root_dir = Path("20-50/20-50")  # raíz del dataset
output_dir = Path("all_images")  # carpeta donde estarán todas las imágenes
output_dir.mkdir(exist_ok=True)

# Diccionario para almacenar datos de train y test
csv_data = {
    "train": [],
    "test": []
}

# Procesa cada conjunto (train y test)
for split in ["train", "test"]:
    split_path = root_dir / split
    for age_dir in split_path.iterdir():
        if age_dir.is_dir():
            age = age_dir.name
            for img_path in age_dir.glob("*.jpg"):
                # Genera nuevo nombre y ruta
                new_filename = img_path.name
                new_path = output_dir / new_filename

                # Renombra si hay conflicto
                if new_path.exists():
                    base, ext = os.path.splitext(new_filename)
                    new_filename = f"{base}_{age}{ext}"
                    new_path = output_dir / new_filename

                # Copia la imagen a all_images/
                shutil.copy(img_path, new_path)

                # Ruta relativa para el CSV
                relative_path = os.path.relpath(new_path, start=".")
                
                # Añade entrada al CSV correspondiente
                csv_data[split].append({
                    "file": new_filename,
                    "path": relative_path,
                    "age": age
                })

print(f"Train: {len(csv_data['train'])} imágenes")
print(f"Test: {len(csv_data['test'])} imágenes")

# Guarda CSVs
for split in ["train", "test"]:
    with open(f"{split}.csv", mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "path", "age"])
        writer.writeheader()
        writer.writerows(csv_data[split])
