from pakudex import Pakudex
def print_menu():
    print("""Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit""")
    #Copy pasted """ print statement for simplicity!
if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    print("Enter max capacity of the Pakudex:")
    #Greeting, welcome to my program!
    while True:
    #The try block will test out valid input for capacity. You can have as many as you want! (still, all you need is one "a" to conqueor the observed universe.)
        try:
            capacity = int(input())
            if capacity <= 0:
                raise ValueError
            #check if capacity is positive. you cannot "owe" or borrow pakuris and conquer the universe.UNFORTUNATE.
            break
        except ValueError:
            #catch other types of inputs.
            print("Please enter a valid size.")
            print("Enter max capacity of the Pakudex:")
    pakudex = Pakudex(capacity)
    #welcome to Pakudex: species evolve and conqueor! or be a peace lover. Up to you.
    print("The Pakudex can hold",pakudex.capacity,"species of Pakuri.")
    while True:
        #print the menu and ask what user want to do.
        print_menu()
        option = input("What would you like to do?")
        try:
        #Try and except block. I am really trying to practice it!
            option = int(option)
        except ValueError:
            print("Unrecognized menu selection!")
            continue
        #options can be seen when the menu was printed.
        if option == 1:
            if pakudex.pakudex != None:
                #check if there are any pakuri captured.
                list_pakuri = ""
                #this line and two lines below put into desired format of number and name.
                for i, v in enumerate(pakudex.species_array):
                    list_pakuri += str(i+1)+". "  +v + " "
                print("Pakuri In Pakudex:",list_pakuri)
            else:
                print("No Pakuri in Pakudex yet!")
        elif option == 2:
        #show the attributes of a specie by name.
            species = input("Enter the name of the species to display:")
            if pakudex.species_array!= None and species in pakudex.species_array:
                #check if pakuri exists.
                stats = pakudex.get_stats(species)
                print(f'Species: {species}')
                print(f'Attack: {stats[0]}')
                print(f'Defense: {stats[1]}')
                print(f'Speed: {stats[2]}')
                #stat is a list returned by get_stats. Then we will print each attributes in this order (species,atk,dfs,spd)
            else:
                print("Error: No such Pakuri!")
        elif option == 3:
        #Catch a pakuri!
            if pakudex.size >= pakudex.capacity:
                print("Error: Pakudex is full!")
            #you probably never have to worry about pakudex is full because you can have as many as you want!
            #if pakudex is not full, then procceed to capture process.
            else:
                species = input("Enter the name of the species to add:")
                pakudex.add_pakuri(species)
        elif option == 4:
            species = input("Enter the name of the species to evolve:")
            species = pakudex.evolve_species(species)
            #Evolution! the option that makes you desired pakuri be come a unbeatable beast.
        elif option == 5:
            #sort, as indicated in pakudex file.
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif option == 6:
            #goodbye!
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")
        #capture any number that are not valid
    else:
            print("Unrecognized menu selection!")
        #capture everything other than number.
