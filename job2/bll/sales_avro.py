import os
import fastavro
import json
from typing import Tuple, Union


# Функція для створення Avro-схеми
def create_avro_schema() -> dict:
    schema = {
        "type": "record",
        "name": "Sale",
        "fields": [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"}
        ]
    }
    return schema


def process_data(raw_dir: str, stg_dir: str) -> Tuple[str, int]:
    # Перевірка наявності директорій raw_dir та stg_dir
    if not os.path.exists(raw_dir):
        return f"Raw directory '{raw_dir}' does not exist.", 400
    if not os.path.exists(stg_dir):
        return f"STG directory '{stg_dir}' does not exist.", 400

    # Очистка вмісту директорії stg_dir
    for filename in os.listdir(stg_dir):
        file_path = os.path.join(stg_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Зчитування та перетворення JSON файлів у формат Avro
    avro_schema = create_avro_schema()

    for filename in os.listdir(raw_dir):
        if filename.endswith('.json'):
            raw_file_path = os.path.join(raw_dir, filename)
            stg_file_path = os.path.join(stg_dir, f"sales_{filename[:-5]}.avro")

            with open(raw_file_path, 'r') as raw_file, open(stg_file_path, 'wb') as stg_file:
                # Зчитування даних з JSON
                sales_data = json.load(raw_file)

                # Створення Avro файлу та запис даних
                fastavro.writer(stg_file, schema=avro_schema, records=sales_data)

    return "Data processing completed successfully.", 201
