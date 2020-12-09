import random
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
        super().__init__('Orc', 6, 3, 4, 4, 0.10)

class Troll(Monster):
    def __init__(self):
        super().__init__('Troll', 2, 4, 7, 2, 0.05)
    

class Treasures:
    def __init__(self, treasure, value):
        self.treasure = treasure
        self.value = value

coins = Treasures("Coins", 2)
money_pouch = Treasures("Money pouch", 6)
gold_jewelry = Treasures("Gold Jewelry", 10)
gems = Treasures("Gems", 14)
small_treasure_chest = Treasures("Small treasure chest", 20)



treasure_list = [str(coins.treasure), str(money_pouch.treasure), str(gold_jewelry.treasure), str(gems.treasure), str(small_treasure_chest.treasure), "No treasure"]
def random_treasurs():
    random_treasure = random.choices(treasure_list, weights=[40, 20, 15, 10, 5, 10], k=1)
    print(random_treasure)



Monster_list = [str(GiantSpider), str(Skeletton), str(Orc), str(Troll), "inget monster"]
def random_monsters():
    random_monster = random.choices(Monster_list, weights=[20, 15, 10, 0.05, 55], k=1)
    print(random_monster)


random_monsters()
random_treasurs()