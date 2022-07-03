class Menu:
    def __init__(self):
        self.item = None
        self.rate = None

    def add(self, item, rate):
        self.item = item
        self.rate = rate


    def show(self):
        print(self.item, self.rate)


m = Menu()  # Menu is a class

m.add("idli", 10)
m.show()
m.add("vada", 20)
m.show()
