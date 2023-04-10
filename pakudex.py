from pakuri import Pakuri
class Pakudex:
    def __init__(self,capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.pakudex = None
        self.species_array = None
    #this is the Pakudex. The collection of pakuris. The initial values are set, and the default capacity is 20.
    def get_size(self):
        return self.size
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        return self.species_array
    #this is the list containing name of pakuris
    def get_stats(self,species):
        if self.species_array != None:
            for i in self.pakudex:
                if i.species == species:
                    return [i.attack,i.defense,i.speed]
    #this function returns the attack, defense, and speed of a specific pakuri.
        return None
    #return None if no such pakuri.
    def sort_pakuri(self):
        if self.species_array != None:
            self.pakudex.sort(key=lambda x: x.species)
            self.species_array.sort()
    # this function is to sort pakuri by python default lexological order.
        return True

    def add_pakuri(self, species):
        captured_pakuri = Pakuri(species)
        #convert species into an obeject by Pakuri.
        if self.species_array !=None and species in self.species_array:
            print("Error: Pakudex already contains this species!")
        #check if there are any duplications.
            return False
        if self.pakudex == None:
            self.pakudex = [captured_pakuri]
            self.species_array = [captured_pakuri.species]
            self.size +=1
            print("Pakuri species", captured_pakuri.species, "successfully added!")
        #add the first pakuri. By adding first pakuri, the program will convert species_array and pakudex from None to a list.
        #This action will increment the size by one.
        else:
        # similar implementation like lines above. We can now append because those lists are created.
            self.pakudex.append(captured_pakuri)
            self.species_array.append(captured_pakuri.species)
            self.size +=1
            print("Pakuri species", captured_pakuri.species, "successfully added!")
        return True
    def evolve_species(self,species):
        if self.species_array != None:
        #check if there are any pakuri in pakudex.
            if species not in self.species_array:

                print("Error: No such Pakuri!")
                return False
        #if the specific pakuri has not been add, return False.
            else:
                for i in self.pakudex:
        #Iterate through pakudex and look for the specific pakuri.
                    if i.species == species:
        ##A pakuri is found! call evolve upon this species and make it stronger!
                        i.evolve()
                        break
                print(species,"has evolved!")
            return i
        return False

# pakudex1 = Pakudex()
# pakudex1.add_pakuri("bikabu")
# pakudex1.add_pakuri("Lalafelloflight")
# pakudex1.add_pakuri("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander")
#-------------------------Yes my friend Kurai is very op but he cannot solo TEA. Even with this length of name. lol
# pakudex1.add_pakuri("TinySnowWolf2077")
# pakudex1.add_pakuri("LalafellofDarkness")
# print(pakudex1.species_array)
# print(pakudex1.get_stats("bikabu"))
# print(pakudex1.evolve_species("bikabu"))
# print(pakudex1.get_stats("Lalafelloflight"))
# print(pakudex1.get_stats("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander"))
# print(pakudex1.get_stats("TinySnowWolf2077"))
# print(pakudex1.get_stats("LalafellofDarkness"))
# print(pakudex1.evolve_species("Lalafelloflight"))
# print(pakudex1.evolve_species("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander"))

# for i in (31415926):
    #(pakudex1.evolve_species("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander")
# print(pakudex1.evolve_species("KuraiKuisverysigoyi.probablythemostoppersonontheworldthatcansolotheepicofalexander"))
#------------------------Okay maybe now he's good enough to solo Tea, with the benediction of Pi god.
# print(pakudex1.evolve_species("TinySnowWolf2077"))
# print(pakudex1.evolve_species("LalafellofDarkness"))
