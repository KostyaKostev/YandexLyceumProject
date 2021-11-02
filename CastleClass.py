elfs = {}
orcs = {}
fn = 'orcs'
sn = 'elfs'


class unit:
    def __init__(self, name, nation, power, health, factor_p):
        self.name = name
        if nation == fn:
            orcs[name] = [str(power), str(health), str(factor_p)]
        else:
            elfs[name] = [str(power), str(health), str(factor_p)]

    def return_name(self):
        return self.name


elf = unit('эльф-копейщик', 'elfs', 1, 1, 0)
orc = unit('гоблин', 'orcs', 1, 1, 0)


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
        return [self.player, self.nation, self.army, self.naim]