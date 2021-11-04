cities= ["Oakland", "Altanta", "New York City", "Seattle","Memphis", "Miami",
"Boston","Los Angeles", "Denver", "New Orleans"]
print(cities)

wildflowers = ["White Clover", "Bellflower", "Bee Balm", "Queen Anne's Lace",
"Field Scabious", "Oxeye Daisy", "Lupine", "Cardinal Flower", "Toadflax","Blanket Flower"]
print (wildflowers)

print(cities[2],cities[3],cities[-2])
print(wildflowers[3],wildflowers[4],wildflowers[7])

cities[0]= "San Francisco"
cities[2]= "Brooklyn"
cities[-3]= "Hollywood"
cities[-5] = "Tampa"
print(cities)

cities.append("Oakland")
cities.extend(["New York City","Los Angeles"])
cities.insert(0,"Miami")
print(cities)

del cities[0]
cities.pop(6)
cities.remove("Memphis")
print(cities)

