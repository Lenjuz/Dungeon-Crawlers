class Monster:
    def __init__(self, monster, initative, endurance, attack, agility, common):
        self.monster = monster
        self.initiative = initative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.common = common
        self.allstats = {'Class': f'{monster}', 'Initative': f'{initative}', 'Endurance': f'{endurance}', 'Attack': f'{attack}', 'Agility': f"{agility}", "Common": f"{common}"}

class GiantSpider(Monster):
    def __init__(self):
        super().__init__('GiantSpider', 7, 1, 2, 3, 0.20)

class Skeletton(Monster):
    def __init__(self):
        super().__init__('Skeletton', 4, 2, 3, 3, 0.15)

class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 6, 3, 4, 4, 0.1)

class Troll(Monster):
    def __init__(self):
        super().__init__('Troll', 2, 4, 7, 2, 0.05)


test_monster = Troll()
print(test_monster.allstats)
