dict_food = {"Chicken" :1.59,"Beef":1.99,"Cheese" :1.00 ,"Milk" : 2.50 }
print (dict_food)

school_supplies = {"notebooks": 6, "pens" :4, "binders" :2, "calculator" :1}


chicken_price = dict_food["Chicken"]
print (chicken_price)

beef_price = dict_food ["Beef"]
print (beef_price)

cheese_price = dict_food ["Cheese"]
print (cheese_price)

milk_price = dict_food ["Milk"]
print (milk_price)

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
print (shoe_inv)

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
print (shoe_inv)

dict_food ["Eggs"] =1.79
dict_food ["Bacon"] = 1.89
dict_food ["Strawberry"] =3.50
print (dict_food)

school_supplies ["highlighters"] =5
school_supplies ["pencils"] = 7
school_supplies ["laptop"] = 1
print (school_supplies) 

shoe_inv ["Jordan "] = 12
shoe_inv ["Nike"] = 10
shoe_inv ["Pumas"] = 8
print (shoe_inv)

del dict_food ["Eggs"] 
del dict_food ["Bacon"]
print (dict_food)

del school_supplies ["highlighters"] 
del school_supplies ["pencils"]
print (school_supplies)

del shoe_inv["Nike"] 
del shoe_inv ["Pumas"]
print (shoe_inv)







