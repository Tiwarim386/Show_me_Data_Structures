import os


def find_files(suffix='', path='.'):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Edge cases
    if path is None:
        return "No path specified"
    elif not isinstance(path, str):
        return "Path isn't a valid path"

    files = []

    # For all files in the current directory

    for file in os.listdir(path):

        # Concatenates the current path and the file
        file_path = os.path.join(path, file)

        # If file is a file (not a subdirectory)
        if os.path.isfile(file_path):

            # If file ends with suffix
            if file.endswith(suffix):
                # Save file's path
                files.append(file_path)

        # If file is a subdirectory (not a file)
        if os.path.isdir(file_path):
            # Recursion - Go into the subdirectory
            new_files = find_files(suffix, file_path)

            # Append new_files to current files
            files.extend(new_files)

    return files


# Edge test cases
print("find_files(, None):", find_files('', None), '\n')
print("find_files(, -1):", find_files('', -1), '\n')

# General test cases
print("find_files(\"\", .):", find_files("", "."), '\n')
print("find_files(\".py\", .):", find_files(".py", "."), '\n')
print("find_files(\".pdf\", .):", find_files(".pdf", "."), '\n')
print("find_files(\".c\", .):", find_files(".c", "."), '\n')
print("find_files(\".gitkeep\", .):", find_files(".gitkeep", "."), '\n')

print(find_files('.c', '.'))
#expected output: ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']

print('----------------------------------------')

print(find_files('', '.'))
#expected output: all files in the path
print('----------------------------------------')

print(find_files('.h', '.'))
#expected output: ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']

print('----------------------------------------')
print(find_files('t1.h', '.'))
#expected output: ['./testdir/t1.h']

print('----------------------------------------')
print(find_files('t1.h')) #if a path is not specified, the default is the current directory
#expected output: ['./testdir/t1.h']


print('----------------------------------------')
print(find_files( path= '.')) #if a suffix is not specified it searches for all files
#expected output: all files in the path
