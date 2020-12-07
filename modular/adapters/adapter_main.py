import modular
import os

from ..modules.mod1 import mod1_adapter
from ..modules.mod1 import gui as mod1_gui


def search_modules():
    _path = os.path.join(os.path.abspath(os.path.dirname(modular.__path__[0])), "modular/modules")

    item_list = [item for item in os.listdir(_path) if (not item.startswith("__")) and (not item.endswith(".pyc"))]

    print("Modules:")
    print(*item_list, sep="\n")

    return item_list


class Adapter:
    def __init__(self):
        self.mod1_adapter = mod1_adapter.GuiAdapter()
        self.mod1_gui = mod1_gui.DenemeGui()

    def run(self):
        self.mod1_adapter.run(self.mod1_gui)