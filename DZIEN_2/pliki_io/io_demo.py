
import json
import csv
import os

# Utwórz katalog na pliki, jeśli nie istnieje
base_path = "io_demo"
os.makedirs(base_path, exist_ok=True)

# Dane do zapisania
sample_data = {
    "name": "Jan Kowalski",
    "age": 30,
    "hobbies": ["czytanie", "jazda na rowerze", "kodowanie","ćwiczenia kalisteniczne"]
}

# --- Operacje na pliku tekstowym ---
txt_file_path = os.path.join(base_path, "sample.txt")
with open(txt_file_path, "w", encoding="utf-8") as f:
    f.write("To jest przykładowy tekst.\nDruga linia tekstu.")

with open(txt_file_path, "r", encoding="utf-8") as f:
    txt_content = f.read()
    print("Zawartość pliku TXT:")
    print(txt_content)

# --- Operacje na pliku CSV ---
csv_file_path = os.path.join(base_path, "sample.csv")
with open(csv_file_path, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "age", "hobby"])
    for hobby in sample_data["hobbies"]:
        writer.writerow([sample_data["name"], sample_data["age"], hobby])

with open(csv_file_path, "r", encoding="utf-8") as csvfile:
    csv_content = csvfile.read()
    print("\nZawartość pliku CSV:")
    print(csv_content)

# --- Operacje na pliku JSON ---
json_file_path = os.path.join(base_path, "sample.json")
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(sample_data, f, indent=4)

with open(json_file_path, "r", encoding="utf-8") as f:
    json_content = f.read()
    print("\nZawartość pliku JSON:")
    print(json_content)
