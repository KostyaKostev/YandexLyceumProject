class Player:
    def __init__(self, name):
        self.name = name
        self.castles = []
        self.army = [0]
        self.pols = []
        self.castle_count = 1

    def add_army(self, l):
        self.army.extend(l)

    def add_castle(self, castle):
        self.castles.append(castle)

    def print_info(self):
        return [str(self.name), self.castle_count, self.army]