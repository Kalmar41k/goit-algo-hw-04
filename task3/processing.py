"""
Модуль є доповненням скрипта task3.py. Має 2 функції:
    log_error(message): Візуалізує помилки червоним кольором з префіксом [ERROR]
    
    visualize_directory_structure(dir_path: str): Візуалізує структуру директорії, 
    відображаючи файли та піддиректорії з використанням кольорів.
"""
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def log_error(message: str):
    """
    Візуалізує помилки червоним кольором з префіксом [ERROR].
    
    Аргументи:
        message (str): Повідомлення, яке потрібно відформатувати.
    """
    print(f"{Fore.RED} [ERROR] {message}")

def visualize_directory_structure(dir_path: str):
    """
    Візуалізує структуру директорії, відображаючи файли та піддиректорії з використанням кольорів.
    
    Аргументи:
        dir_path (str): Шлях до директорії.
    """
    path = Path(dir_path)

    if not path.is_dir():
        log_error(f"{dir_path} не є дійсною директорією.")
        return

    for item in path.rglob("*"):
        if item.is_dir():
            print(Fore.BLUE + f"Папка: {item}")
        else:
            print(Fore.GREEN + f"Файл: {item}")
