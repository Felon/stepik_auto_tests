import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)
print(os.path.abspath(os.path.dirname('file.txt')))
print(os.path.abspath('file.txt'))
#element.send_keys(file_path)