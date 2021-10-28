class Player:
    def __init__(self, name):
        self.name = name
        self.castles = []
        self.army = []
        self.pols = []

    def add_army(self, l):
        self.army.extend(l)

    def add_catle(self, k):
        self.castles.append(k)

    def add_pole(self, p):
        self.pols.append(p)

    def print_info(self):
        return [self.name, self.castles, self.army, self.pols]