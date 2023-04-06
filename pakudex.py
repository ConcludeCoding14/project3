from pakuri import Pakuri
class Pakudex:
    def __init__(self,capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.pakudex = None
        self.species_array = []
    def get_size(self):
        return self.size
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        return self.species_array
    def get_stats(self,species):
        for i in self.pakudex:
            if i.species == species:
                return [i.attack,i.defense,i.speed]
        return None
    def sort_pakuri(self):
        pass
    def add_pakuri(self,species):
        species = Pakuri(species)
        captured_pakuri = species
        if self.size == self.capacity:
            return False
        elif self.pakudex != None and species in self.pakudex:
            return False
        if self.pakudex == None:
            self.pakudex = [captured_pakuri]
            self.species_array.append(captured_pakuri.species)
        else:
            self.pakudex.append(captured_pakuri)
            self.species_array.append(captured_pakuri.species)
        return True
    def evolve_species(self,species):
        if species not in self.species_array:
            return False
        pass

# pakudex1 = Pakudex()
# print(pakudex1.add_pakuri("bikabu"))
# print(pakudex1.add_pakuri("Lalafelloflight"))
# print(pakudex1.add_pakuri("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander"))
# print(pakudex1.add_pakuri("TinySnowWolf2077"))
# print(pakudex1.add_pakuri("LalafellofDarkness"))
# print(pakudex1.species_array)
# print(len(pakudex1.species_array))
# print(pakudex1.get_stats("bikabu"))
# print(pakudex1.get_stats("Lalafelloflight"))
# print(pakudex1.get_stats("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander"))
# print(pakudex1.get_stats("TinySnowWolf2077"))
# print(pakudex1.get_stats("LalafellofDarkness"))