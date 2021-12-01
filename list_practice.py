cities= ["Oakland", "Altanta", "New York City", "Seattle","Memphis", "Miami",
"Boston","Los Angeles", "Denver", "New Orleans"]


wildflowers = ["White Clover", "Bellflower", "Bee Balm", "Queen Anne's Lace",
"Field Scabious", "Oxeye Daisy", "Lupine", "Cardinal Flower", "Toadflax","Blanket Flower"]




cities[0]= "San Francisco"
cities[2]= "Brooklyn"
cities[-3]= "Hollywood"
cities[-5] = "Tampa"


cities.append("Oakland")
cities.extend(["New York City","Los Angeles"])
cities.insert(0,"Miami")


del cities[0]
cities.pop(6)
cities.remove("Memphis")


def print_city(list) :
    for el in list:
        print(el)
    return "All cities printed"

def reorganize_list(list):
    # [0,1,2,3,4,5]
    print(list)
    counter = 0

    while counter < len(list):
        item1 = list[counter]
        item2 = list[counter +1]

        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter +1 == len(list) -1:
            break
        else:
            list.remove(item1)
            list.append(item1)
            counter += 1

    
    return list
def sort_list (list):
    return sorted(list)



print(print_city(cities))
print(sort_list(wildflowers))



