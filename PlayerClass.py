class Player:
    def __init__(self, name):
        self.name = name
        self.castles = []
        self.army = [0]
        self.pols = []
        self.castle_count = 0

    def add_army(self, l):
        self.army.extend(l)

    def add_castle(self, k):
        self.castles.append(k)
        self.castle_count += 1

    def add_pole(self, p):
        self.pols.append(p)

    def print_info(self):
        return [str(self.name), self.castle_count, self.army, self.pols]