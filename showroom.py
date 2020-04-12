# create an empty set named showroom
showroom = set()
# Add four of your favorite car model names to the set
showroom = {'Altima', 'Thunderbird', 'Dart', 'Accord'}
# Print the length of your set
print(len(showroom))
# Pick one of the items in your show room and add it to the set again
showroom.add("Altima")
# Print your showroom. Notice how there's still only one instance of that model in there
print(showroom)
# Using update(), add two more car models to your showroom with another set
showroom.update({"Prius", "Countryman"})
print(showroom)
# You've sold one of your cars. Remove it from the set with the discard() method
showroom.discard('Accord')
print(showroom)

print()
# Acquiring more cars
"""
Now create another set of cars in a variable junkyard. Someone who owns a 
junkyard full of old cars has approached you about buying the entire inventory. 
In the new set, add some different cars, but also add a few that are the same 
as in the showroom set.
"""
junkyard = {"Dart", "Countryman", "Camry", "F150", "Civic"}
print('junkyard: ', junkyard)
# Use the intersection method to see which cars exist in both the showroom and that junkyard
common_cars = showroom.intersection(junkyard)
print('common_cars: ', common_cars)
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom
union_cars = junkyard.union(showroom)
print('union cars: ', union_cars)
# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom
for car in junkyard:
    if car not in showroom:
        union_cars.discard(car)
print('updated union_cars: ', union_cars)