groceries = {"Chicken" :1.59,"Beef":1.99,"Cheese" :1.00 ,"Milk" : 2.50 }


school_supplies = {"notebooks": 6, "pens" :4, "binders" :2, "calculator" :1}


chicken_price = groceries["Chicken"]


beef_price = groceries ["Beef"]


cheese_price = groceries ["Cheese"]

milk_price = groceries ["Milk"]


notebooks = school_supplies ["notebooks"]
pens = school_supplies ["pens"]
binders = school_supplies ["binders"]
calculator = school_supplies ["calculator"]

shoe_inv = {
    "Jordan 13" :1,
    "Yeezy" : 8,
    "Foamposite" : 19,
    "Air Max": 5,
    "SB Dunk " : 20}


shoe_inv ["SB Dunk "] -=2
shoe_inv [ "Yeezy"] += 1
shoe_inv ["SB Dunk "] +=7
shoe_inv ["Yeezy"] +=7
shoe_inv ["Air Max"] +=7
shoe_inv ["Foamposite"] +=7
shoe_inv [ "Jordan 13"] +=7

shoe_inv ["SB Dunk "] -=3
shoe_inv ["Yeezy"] -=3
shoe_inv ["Air Max"] -=3
shoe_inv ["Foamposite"] -=3
shoe_inv [ "Jordan 13"] -=3


groceries ["Eggs"] =1.79
groceries ["Bacon"] = 1.89
groceries ["Strawberry"] =3.50


school_supplies ["highlighters"] =5
school_supplies ["pencils"] = 7
school_supplies ["laptop"] = 1


shoe_inv ["Jordan "] = 12
shoe_inv ["Nike"] = 10
shoe_inv ["Pumas"] = 8


del groceries ["Eggs"] 
del groceries ["Bacon"]


del school_supplies ["highlighters"] 
del school_supplies ["pencils"]


del shoe_inv["Nike"] 
del shoe_inv ["Pumas"]

def total_price(food_item, food_item2):
    total = groceries[food_item] + groceries[food_item2]
    return total 

def price_diff(food_item, food_item2):
    diff=groceries [food_item] - groceries [food_item2]
    return abs(diff)
def shoe_restock (shoe, num) :
    shoe_inv [shoe] *= num
    return shoe_inv

def clearance_sale (shoe, num) :
    shoe_inv [shoe] //= num
    return shoe_inv

def supply_search(dict):
    largest= 0
    supply = ''

    for key in dict.keys():
        if dict[key] > largest:
            largest = dict [key]
            supply = key
   
    return (supply, largest)


print(total_price ("Beef","Cheese"))
print(price_diff ("Beef","Cheese"))
print(shoe_restock ("Yeezy",3))
print(clearance_sale ("SB Dunk ",2))
print(supply_search (school_supplies))






