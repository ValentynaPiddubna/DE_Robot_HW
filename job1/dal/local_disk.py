import os
import json


def clear_directory(raw_dir: str) -> None:
    for file_name in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def save_data_to_file(data: dict, date_str: str, raw_dir: str, file_index: int) -> None:
    file_name = f'sales_{date_str}_{file_index}.json'
    file_path = os.path.join(raw_dir, file_name)

    try:
        with open(file_path, 'w') as file:
            file.write(json.dumps(data))
    except Exception as e:
        print(f"Error saving file {file_path}: {str(e)}")
