
print("hello" + "world")

print("hello", "world" + " I love" + " python")

fruit = "apple"

fruit *=20

print(fruit)

example = "\tprofessor H   \t\t\t\n hello :) \t"
print(example)
print(example.strip())
print(example.rstrip())
print(example.lstrip())


name = "big blue"
print(name)
print(name.capitalize())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.lower())
print(name.isdigit())



cities = []
for i in range(3):
    city = input("Enter the city you are from: ").lower()
    if city.lower() in cities:
        pass
    else:
        cities.append(city)

print("cities: ", cities)