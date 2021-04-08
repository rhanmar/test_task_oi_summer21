import hashlib
import os
from datetime import datetime
import argparse
import sys


my_parser = argparse.ArgumentParser()  # Create the parser
my_parser.add_argument('--delete', action='store_true')  # Add --delete
my_parser.add_argument('Path', metavar='path', type=str, help='the path to dir')  # Add arguments
args = my_parser.parse_args()  # Execute the parse_args() method


def find_size_unit(size):
    power = 2 ** 10
    counter = 0
    units = {
        0: 'bytes',
        1: 'KB',
        2: 'MB',
        3: 'GB',
        4: 'TB'
    }
    while size > power:
        size /= power
        counter += 1
    return size, units[counter]


def show_part_of_files(files):
    sum_of_filesizes = 0
    duplicated_files = []
    for file in files:
        sum_of_filesizes += files[file]['size']
        created = datetime.fromtimestamp(files[file]['created']).strftime('%d-%m-%Y')
        duplicated_files.append(f"{file} (Created: {created})")

    size, unit = find_size_unit(sum_of_filesizes)
    size = round(size, 2)

    print(f"Size: {size} {unit}")
    for index, file in enumerate(duplicated_files):
        print(f"[{index + 1}]: {file}")
    print('-' * 70)
    return None


def remove_duplicates(files):
    for file_hash in files:
        duplicated_files = list(files[file_hash]['files'].keys())
        show_part_of_files(files[file_hash]['files'])

        print('Choose file to keep by entering its number or press enter to skip it')
        while True:
            index_to_keep = input()
            if len(index_to_keep) == 0:
                break
            elif not index_to_keep.isnumeric():
                print('Not valid!')
                continue
            elif int(index_to_keep) < 0:
                print("Can't be negative!")
                continue
            elif int(index_to_keep) - 1 > len(duplicated_files):
                print('Wrong number!')
                continue
            else:
                index_to_keep = int(index_to_keep)
                file_to_keep = duplicated_files.pop(index_to_keep - 1)
                print(f"File {file_to_keep} was kept\n")
                for file in duplicated_files:
                    os.remove(file)
                break
    return None


def remove_not_duplicates(files):
    result = {}
    for file_hash in files:
        if files[file_hash]['count'] > 1:
            result[file_hash] = files[file_hash]
    return result


def show_all_files(files):
    for file_hash in files:
        show_part_of_files(files[file_hash]['files'])
    return None


def get_files(path):
    result = {}
    files = []

    for root, _, f in os.walk(path):
        for file in f:
            filepath = os.path.join(root, file)
            files.append(os.path.abspath(filepath))

    for filename in files:
        hash_md5 = hashlib.md5()
        try:
            with open(filename, 'rb') as f:
                while True:
                    file_data = f.read(8192)
                    if not file_data:
                        break
                    hash_md5.update(file_data)
        except PermissionError:
            continue
        file_hash = hash_md5.hexdigest()
        if file_hash not in result:
            result[file_hash] = {}
            result[file_hash]['count'] = 1
            result[file_hash]['files'] = {}
            result[file_hash]['files'][filename] = {}
            result[file_hash]['files'][filename]['size'] = os.path.getsize(filename)
            result[file_hash]['files'][filename]['created'] = os.path.getctime(filename)
        else:
            result[file_hash]['count'] += 1
            result[file_hash]['files'][filename] = {}
            result[file_hash]['files'][filename]['size'] = os.path.getsize(filename)
            result[file_hash]['files'][filename]['created'] = os.path.getctime(filename)
    return result


def main():
    path = args.Path
    if not os.path.isdir(path):
        print('Wrong path!')
        sys.exit()
    files = get_files(path)
    files = remove_not_duplicates(files)
    if args.delete is True:
        # INTERACTIVE REMOVING
        remove_duplicates(files)
    else:
        # OUTPUT
        show_all_files(files)


main()
