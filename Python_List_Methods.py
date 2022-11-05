#Choices of the menu
def functionsMenu():
        list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
        print("Given the List of", list)
        print("================================================================")
        print("List of list methods in Python")
        print("================================================================")
        print("1. Add an element [uses append()]")
        print("2. Insert an element [uses insert()]")
        print("3. Modify an element [uses pop(), insert() and index()]")
        print("4. Delete an element [uses remove()]")
        print("5. Arrange in ascending order [uses sort()]")
        print("6. Arrange in descending order [uses sort() and reverse()]")
        print("7. Exit the program")
        print("What do you want to do with this list? ")
        print("================================================================")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    Add()
                elif choice == 2:
                    Insert()
                elif choice == 3:
                    Modify()
                elif choice == 4:
                    Delete()
                elif choice == 5:
                    Ascending()
                elif choice == 6:
                    Descending()
                elif choice == 7:
                    break
                else:
                    print("Invalid choice please enter numbers from 1-7")
                    functionsMenu()
            except ValueError:
                print("Invalid choice please enter numbers from 1-7")
                print("================================================================")
        exit()


#List functions
def Add():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    add = int(input("What value do you want to add to the list? "))
    list.append(add)
    print("The new list: ")
    print(list)
    Continue()

def Insert():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    index_ins = int(input("Enter the index number of the value you want to put in: "))
    value_ins = int(input("Enter the value you want to put in: "))
    list.insert(index_ins, value_ins)
    print("The new list: ")
    print(list)
    Continue()

def Modify():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    value_mod = int(input("Enter the value you want to modify: "))
    index_mod = list.index(value_mod)
    list.pop(index_mod)
    modified_value = int(input("Enter the value you want to replace with: "))
    list.insert(index_mod, modified_value)
    print("The new list: ")
    print(list)
    Continue()

def Delete():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    value_del = int(input("Enter the value you want to remove: "))
    list.remove(value_del)
    print("The new list: ")
    print(list)
    Continue()

def Ascending():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    print("The current list of numbers are:")
    print(list)
    list.sort()
    print("Sorted in Ascending order: ")
    print(list)
    Continue()

def Descending():
    list = [33, 37, 30, 133, 333, 3033, 3333, 5, 27]
    print("The current list of numbers are:")
    print(list)
    list.sort()
    list.reverse()
    print("Sorted in Descending order: ")
    print(list)
    Continue()

def Continue():
    print("================================================================")
    cont = input("Do you want to continue? (enter anything or enter no) ")
    print("================================================================")
    while cont.lower() not in ("no"):
        functionsMenu()
    if cont == "no":
        exit()

#main
functionsMenu()
