from colorama import Fore
from pathlib import Path
import sys

# створення об'єкту для заданого шляху
path = sys.argv[1]
parent_folder_path = Path(path)


#
def parse_folder(path):
    # Перевірка, чи шлях існує та чи є це директорія
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Path '{path}' is not exist or is not folder.")
        return
    # Обхід всіх директорій та файлів у поточній директорії
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.BLUE + f'Folder: {element.name}')
            # рекурсія
            parse_folder(element)
        if element.is_file():
            print(Fore.MAGENTA + f'File: {element.name}')


# виклик скрипту
parse_folder(parent_folder_path)
