import os

dir = raw_input('Search Dirname : ')
extension = raw_input('Search Extension : ')

def search(dirname):
        try:
                filenames = os.listdir(dirname)
                for filename in filenames:
                        full_filename = os.path.join(dirname, filename)
                        if os.path.isdir(full_filename):
                                search(full_filename)
                        else:
                                ext = os.path.splitext(full_filename)[-1]
                                if ext ==extension:
                                        print(full_filename)
        except PermissionError:
                pass
search(dir)
