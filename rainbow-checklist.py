# -*- coding: utf-8 -*-#
#  creating empty list
checklist =[]

#creating CRUD functions for checklist

# CREATE
def create(item):

    # Create item code here
    checklist.append(item)

    return "Added {} to checklist".format(item)

# READ
def read(index):

    # Read code here
    print(checklist[index])

    return checklist[index]

# UPDATE 
def update(index, item):
    
    old = checklist[index]

    # Update code here
    checklist[index] = item

    return "Changed {} to {}".format(old, item)


# DESTROY
def destroy(index):

    removed = checklist[index]
     
    # Destroy code here
    checklist.pop(index)

    return "Removed {} from checklist".format(removed)

# SEE ALL ITEMS
def all_items():

    items = []

    for element in checklist:
        print(element)
        items.append(element)

    return items 

# ADD CHECK MARK TO ITEM
def checked(index):

    unchecked = checklist[index] 

    checklist[index] = "√ " + unchecked 

    return checklist[index]

# USER INPUT FUNCTION 
def user_input(prompt):
     
    entry = input(prompt)

    return entry

#USER CHOICE FUNCTION
def user_choice():

    # initialize variable for while loop
    editing = True

    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, R for read, U for update and D for destroy, A to view all items currently in the checklist and S to select an item with a checkmark. ")

        if choice == "C" or choice == "c":
        
            item = user_input("What item do you wish to create? Type out the name of your desired item. ")

            create(item)

            continue

        elif choice == "R" or choice == "r":

            index = user_input("What item do you wish to read? Give a number for the position of the item. " )

            read(index)

            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("What item do you wish to update? Give a number for the position of the item. " )
        
            new_item = user_input("Type out the name of your new item. ")
        
            update(update_index, new_item)

            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("What item do you wish to delete? Give a number for the position of the item. ")
        
            destroy(delete_index)

            continue
        elif choice == "A" or "a":
            all_items()
            continue
        elif choice == "S" or "s":
            checked_index = user_input("What item do you wish to check off? Give a number for the position of the item. ")
            checked(checked_index)
            continue
        else:

            end = user_input("Do you wish to quit? Enter Y for yes or N for no." )

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:

                continue
def test():

    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # print(all_items())
    # print(checked(0))
    # print(user_input("Is this working?"))
    user_choice()
    
user_choice()



