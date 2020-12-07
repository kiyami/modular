import os
import json


_package_path = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 1)[0]
_json_file = "package_tree.json"


def _path_to_dict(_path):
    for root, dirs, files in os.walk(_path):

        dirs = [d for d in dirs if (not d.startswith("__")) and (not d.endswith(".pyc"))]
        files = [file for file in files if (not file.startswith("__")) and (not file.endswith(".pyc"))]

        _key = root.rsplit(os.sep)[-1]
        tree = {_key: []}
        tree[_key].extend([_path_to_dict(os.path.join(root, d)) for d in dirs])
        tree[_key].extend(files)

        return tree


def update_package_tree():
    os.chdir(_package_path)

    folder_tree = _path_to_dict(_package_path)

    with open(_json_file, mode="w+") as f:
        json.dump(folder_tree, f, indent=2)

    print(json.dumps(folder_tree, indent=2))


if __name__ == "__main__":
    update_package_tree()


"""
def alternative(rootdir):
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir
"""