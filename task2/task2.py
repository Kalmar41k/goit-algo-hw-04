"""
Модуль для виведення інформації про котиків з файлу.
"""
from pathlib import Path

def get_cats_info(path: str) -> list:
    """
    Зчитує інформацію про котів з файлу та повертає список словників з їхніми характеристиками.
    
    Аргументи:
        path (str): Шлях до файлу з даними про котів.

    Повертає:
        list: Список словників з полями id, name і age для кожного кота.
    """
    file_path = Path(path)

    try:
        if not file_path.exists() or not file_path.is_file():
            raise FileNotFoundError(f"Файл {file_path} не існує.")

        with file_path.open("r", encoding="utf-8") as file:
            cats = file.readlines()

            cats_info = []

            for line in cats:
                cat_info = line.split(",")

                cat_info_dict = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2].strip()
                }

                cats_info.append(cat_info_dict)

            return cats_info

    except FileNotFoundError as e:
        print(f"Помилка: {e}")
        return []

    except Exception as e:
        print(f"Невідома помилка: {e}")
        return []

cats_info = get_cats_info("task2/cats.txt")
print(cats_info)
    