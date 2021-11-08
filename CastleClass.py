from UploadFromBD import all_heroes
elfs = {}
orcs = {}
fn = 'orcs'
sn = 'elfs'
sk = ['▼', 1, 4, 15, 350, 0, 'warrior', 'elfs', 3.5]


class unit:
    def __init__(self, text):
        result = []
        for key in all_heroes.keys():
            if text == key:
                result = all_heroes[text]
                if key not in result:
                    result.insert(0, key)
        self.result = result
        print(result)

    def print_info(self):
        return self.result

    def is_alive(self):
        pass

class Castle:
    def __init__(self, nation, player):
        global fn
        global sn
        self.player = player
        self.nation = nation
        self.army = []
        self.naim = {}
        if nation == fn:
            self.naim = orcs
        else:
            self.naim = elfs

    def print_info(self):
        return [self.player, self.nation, self.army]