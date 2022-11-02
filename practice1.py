class Heroes:
    armor = 'латы'
    def __init__(self):
        pass

class Warrior(Heroes):
    def __init__(self, clas, sword, talant, stat1, stat2, stat3):
        self.clas = clas
        self.sword = sword
        self.talant = talant
        self.stat1 = stat1
        self.stat2 = stat2
        self.stat3 = stat3

    def attack (self , damage) :
        self.damage  = damage

class Mage(Heroes):
    def __init__(self, clas, sword, talant, stat1, stat2, stat3):
        super().__init__()
        self.clas = clas
        self.sword = sword
        self.talant = talant
        self.stat1 = stat1
        self.stat2 = stat2
        self.stat3 = stat3
    def attack(self, damage):
        self.damage = damage

class Assassin(Heroes):
    def __init__(self, clas, sword, talant, stat1, stat2, stat3):
        super().__init__()
        self.clas = clas
        self.sword = sword
        self.talant = talant
        self.stat1 = stat1
        self.stat2 = stat2
        self.stat3 = stat3
    def attack(self, damage):
        self.damage = damage


war = Warrior ('Воин','Экскалибур', 'Ярость берсерка', '120','43','22')
war.attack(182)
mag = Mage ('Маг', 'Огненный посох', 'Метеоритный дождь', '19','37','120')
mag.attack(102)
creed = Assassin('Убийца','Астральные клинки', 'Череда убийств', '64', '112','39')
creed.attack(133)

print(f'Класс : {war.clas} \nОружие: {war.sword} \nОсобый навык: {war.talant} \nСила : {war.stat1} \nЛовкость : {war.stat2} \nИнтелект : {war.stat3} \nУрон : {war.damage}')
print('---'*27)
print(f'Класс : {mag.clas} \nОружие: {mag.sword} \nОсобый навык: {mag.talant} \nСила : {mag.stat1} \nЛовкость : {mag.stat2} \nИнтелект : {mag.stat3} \nУрон :{mag.damage}')
print('---'*27)
print(f'Класс : {creed.clas} \nОружие: {creed.sword} \nОсобый навык: {creed.talant} \nСила : {creed.stat1} \nЛовкость : {creed.stat2} \nИнтелект : {creed.stat3} \nУрон :{creed.damage}')
print('---'*27)