"""
Модуль для обчислення загальної та середньої заробітної плати з файлу.
"""
from pathlib import Path

def total_salary(path: str) -> tuple:
    """
    Обчислює загальну та середню заробітну плату на основі даних у файлі.

    Аргументи:
        path (str): Шлях до файлу, який містить дані про заробітну плату.

    Повертає:
        tuple: Кортеж, що містить два значення:
            Загальна сума заробітної плати (float).
            Середня заробітна плата (float).

    Винятки:
        FileNotFoundError: Якщо файл за вказаним шляхом не існує або це не файл.
        Exception: У випадку інших невідомих помилок (наприклад, формат файлу некоректний).
    
    При виникненні помилки функція повертає кортеж (0, 0).
    """
    file_path = Path(path)

    try:
        if not file_path.exists() or not file_path.is_file():
            raise FileNotFoundError(f"Файл {file_path} не існує.")

        with file_path.open("r", encoding="utf-8") as file:
            salary_list = file.readlines()

            salary_list = [float(line.split(",")[1]) for line in salary_list]
            sum_salary = sum(salary_list)
            avg_salary = sum_salary / len(salary_list)

            return (sum_salary, avg_salary)

    except FileNotFoundError as e:
        print(f"Помилка: {e}")
        return (0, 0)

    except Exception as e:
        print(f"Невідома помилка: {e}")
        return (0, 0)

total, average = total_salary("task1/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
