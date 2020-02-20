import os
import sys
from os.path import join, getsize


def walk_matching(path='.', should_exclude=None):
    for root, dirs, files in os.walk(path):
        for directory in list(dirs):
            if should_exclude(directory):
                dirs.remove(directory)
        yield root, dirs, files


def file_size(path='.'):
    def is_tools_dir(directory):
        return directory in ('.idea', '.git', '.tox')

    for root, dirs, files in walk_matching(path=path, should_exclude=is_tools_dir):
        files_size = sum([getsize(join(root, name)) for name in files])
        print(root, ' size: ', files_size, ' bytes')


if __name__ == '__main__':
    file_size(path=sys.argv[1] if len(sys.argv) > 1 else '.')
