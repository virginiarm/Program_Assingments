# creating empty list
checklist=[]

#creating CRUD functions for checklist

# CREATE
def create(item):
    #Create item code here
    checklist.append(item)

    return "Added {} to checklist". format(item)

# READ
def read(index):

    #Read code here
   print(checklist[index])

   return checklist[index]

# READ
def read (index):

    #Read code here
    print(checklist[index])

    return checklist[index]

# UPDATE 
def update(index,item):
    
    old=checklist[index]

    return "Changed {} to {}".format(old,item)


# DESTROY
def destroy(index):

    removed = checklist[index]
     
    #Destroy code here
    checklist.pop(index)

    return "Removed {} from checklist".format(removed)

#GET AKK ITEMS IN LIST
def all_items():
    items = []
    for el in checklist:
        print(el)
        items.append(el)
    
    return items

#ADD CHECK MARK TO ITEM
def checked(index):
    unchecked = checklist[index]
    checklist[index] = "  " + unchecked

    return checklist[index]

# USER INPUT FUNCTION 
def user_input(prompt):

    entry = input (prompt)
    
    return entry

#USER CHOICE FUNCTION
def user_choice():

    choice = user_input("Which function would you like to use? Enter C for create, R for read and D for destroy. ")

    if choice == "C" or "c":
        
        item = user_input("What item do you wish to create? Type out the name of your desired item. ")

        create(item)

    elif choice == "R" or "r" :

        index = user_input ("What item do you wish to read? Give a number for the position of the item." )

        read(index)

    elif choice == "U" or "u" :

        update_index = user_input("What item do you wish to update? Give a number for the position of the item." )
        
        new_item = user_input("Type out the name of your new item.")
        
        update(update_index,new_item)

    elif choice == "D" or "d" :

        delete_index = user_input("What item do you wish to delete? Give a number for the position of the item.")
        
        destroy(delete_index)


def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(all_items())
    print(checked(0))

    user_choice()
test()



