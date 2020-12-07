

class Container1:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        print("item added", item)


class Container2:
    def __init__(self):
        self.items = []

    def drawItem(self, item):
        self.items.append(item)
        print("item added", item)


class DenemeGui:
    def __init__(self):
        self.container_1 = Container1()
        self.container_2 = Container1()
        self.container_3 = Container2()
        self.container_4 = Container2()


        self.containers_dict = {"sahıs_tipi": [self.container_1, "addItem"],
                                "isim": [self.container_2, "addItem"],
                                "h_ici": [self.container_3, "drawItem"],
                                "h_sonu": [self.container_4, "drawItem"],}
