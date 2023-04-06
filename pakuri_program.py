from pakudex import Pakudex
def print_menu():
    print("""Pakudex Main Menu
    -----------------
    1.List
    2.Show
    3.Add
    4.Evolve
    5.Sort
    6.Exit""")
if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    print("Enter max capacity of the Pakudex:")
    while True:
        try:
            capacity = int(input("Enter the capacity: "))
            break
        except ValueError:
            print("Please enter a valid integer value.")
    pakudex = Pakudex(capacity)
    print("The Pakudex can hold",pakudex.capacity,"species of Pakuri")
    while True:
        print_menu()
        option = input("What would you like to do?")
        if option.isdigit():
            option = int(option)
            if option == 1:
                if pakudex.pakudex != None:
                    print(pakudex.species_array)
                else:
                    print("No Pakuri in Pakudex yet!")
            elif option == 2:
                species = input("Enter the name of the species to display:")
                if species in pakudex.species_array:
                    stats = pakudex.get_stats(species)
                    print(f'Speices: {species}')
                    print(f'Attack: {stats[0]}')
                    print(f'Defense: {stats[1]}')
                    print(f'Speed: {stats[2]}')
                else:
                    print("You don't have",species)
            elif option == 3:
                species = input("Enter the name of the species to add:")
                pakudex.add_pakuri(species)
            elif option == 4:
                species = input("Enter the name of the species to evolve:")
                if species in pakudex.species_array:
                    species = pakudex.evolve_species(species)
                else:
                    print("You don't have",species)
            elif option == 5:
                pass
            elif option == 6:
                break
            else:
                print("Unrecognized menu selection!")
        else:
                print("Unrecognized menu selection!")

#update?