from os import listdir, getcwd
from os.path import isfile, join

read_file_name = 'readTextExample'
write_file_name = 'writeTextExample'

with open(read_file_name, 'r',encoding='utf-8') as file:
    for line in file.readlines():
        print(line)

with open(write_file_name, 'w',encoding='utf-8') as file:
    file.write("Hi this is a line")
    file.write(" ,this is the rest of the line")
    file.write(".\nThis is another line")


def list_all_files_in_a_directory(directory_name):
    return [f for f in listdir(directory_name) if isfile(join(directory_name, f))]

for file in list_all_files_in_a_directory(getcwd()):
    print(file)