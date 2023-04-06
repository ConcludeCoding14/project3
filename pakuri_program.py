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
        capacity = input()
        if capacity.isdigit():
            capacity = int(capacity)
            break
        else:
            print("Please enter a valid size.")
            continue
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
                stats = pakudex.get_stats(species)
                print(f'Speices: {species}')
                print(f'Attack: {stats[0]}')
                print(f'Defense: {stats[1]}')
                print(f'Speed: {stats[2]}')
            elif option == 3:
                species = input("Enter the name of the species to add:")
                pakudex.add_pakuri(species)
            elif option == 4:
                input("Enter the name of the species to evolve:")
            elif option == 5:
                pass
            elif option == 6:
                break
            else:
                print("Unrecognized menu selection!")
        else:
                print("Unrecognized menu selection!")

