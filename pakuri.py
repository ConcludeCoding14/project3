class Pakuri:
    def __init__(self,species):
        self.species = species
        self.attack = (len(species)*7)+9
        self.defense = (len(species)*5)+17
        self.speed = (len(species)*6)+13
    def get_species(self):
        return self.species
    def get_attack(self):
        return self.attack
    def get_defense(self):
        return self.defense
    def set_attack(self,new_attack):
        self.attack = new_attack
    def evolve(self):
        self.attack = self.attack*2
        self.defense = self.defense*4
        self.speed = self.speed*3
    def __str__(self):
        return f'the attack of {self.species} is {self.attack}, defense is {self.defense},and speed is {self.speed}'
    #update?