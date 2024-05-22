from os import path

print(path.abspath(''))

file_path = path.abspath('') + '/empty.txt'

print(file_path)