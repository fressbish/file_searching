import os
from termcolor import cprint, colored
import nltk


# files_count = 0

needed_path = []
path_count = 0


def search_engine():

    global needed_path
    print('write file name')
    needeed_file = str(input())
    needeed_file = needeed_file.lower()

    # dir - directory
    # dirnames - folders
    for dirpath, folders, filenames in os.walk(path):
        cprint(dirpath, color='white')
        cprint(folders, color='yellow')
        cprint(filenames, color='cyan')
        print('\n')
        # files_count += len(filenames)

        for filename in filenames:

            filename = filename.lower()

            difference = nltk.edit_distance(needeed_file, filename)
            relation = difference / len(filename)

            if relation < 0.4:
                needed_path.append(dirpath)
                global path_count
                path_count += 1
                print('\n', 'found')


print('\n')

print('write disk')
disk = input()
print('write place')
place = input()
path = '{disk}:\\{place}'.format(disk=disk, place=place)

search_engine()

if needed_path:
    cprint('file was found!', color='blue')
    print("file's count is ", path_count)
    needed_path = str(needed_path)
    print(colored('path is: ', color='blue'), needed_path)
else:
    cprint('nothing was found...', color='red')
