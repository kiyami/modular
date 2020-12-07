import modular
import os


def generate_package_path(path):
    return os.path.join(os.path.abspath(os.path.dirname(modular.__path__[0])), path)