from .config import contents, relations
from .gui import DenemeGui


class GuiAdapter:
    @staticmethod
    def _fill_gui(target_container, method, item_list):
        for item in item_list:
            getattr(target_container, method)(item)

    @staticmethod
    def run(gui):
        for keyword, target_container_and_method in gui.containers_dict.items():
            items_to_fill = contents[keyword][0]
            target_container, method = target_container_and_method
            GuiAdapter._fill_gui(target_container, method, items_to_fill)
