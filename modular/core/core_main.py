from ..gui.gui_main import MainGui

from ..adapters.adapter_main import search_modules
from ..adapters.adapter_main import Adapter


def main():
    print("Core main..")
    search_modules()

    adp = Adapter()
    adp.run()