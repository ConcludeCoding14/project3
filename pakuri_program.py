from pakudex import Pakudex

def print_menu():
    print("""
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
""")

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            pakudex = Pakudex(capacity)
            break
        except ValueError:
            print("Please enter a valid integer value.")
    print("The Pakudex can hold", pakudex.capacity, "species of Pakuri.")
    while True:
        print_menu()
        option = input("What would you like to do? ")
        if option.isdigit():
            option = int(option)
            if option == 1:
                if pakudex.size() > 0:
                    print("Pakuri in Pakudex:")
                    print(*pakudex.get_species(), sep='\n')
                else:
                    print("No Pakuri in Pakudex yet!")
            elif option == 2:
                species = input("Enter the name of the species to display: ")
                if species in pakudex.get_species():
                    stats = pakudex.get_stats(species)
                    print(f"Species: {species}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")
                else:
                    print(f"You don't have a {species}!")
            elif option == 3:
                species = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(species):
                    print(f"Successfully added {species}!")
                else:
                    print(f"Pakudex is full!")
            elif option == 4:
                species = input("Enter the name of the species to evolve: ")
                if species in pakudex.get_species():
                    if pakudex.evolve_pakuri(species):
                        print(f"{species} has evolved!")
                    else:
                        print(f"{species} is already at its highest stage!")
                else:
                    print(f"You don't have a {species}!")
            elif option == 5:
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")
            elif option == 6:
                print("Thanks for using Pakudex: Tracker Extraordinaire!")
                break
            else:
                print("Unrecognized menu selection!")
        else:
            print("Unrecognized menu selection!")
