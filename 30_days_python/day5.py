#Create an empty tuple
tup=()
print(tup)
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tup1=("toji","yuta","yuji")
tup2=("kaori","rukia","masaki")
#Join brothers and sisters tuples and assign it to siblings
siblings=tup1+tup2
print(siblings)
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
tup3=("aizen","yoruichi")
family_members=siblings+tup3
print(family_members)
#Unpack siblings and parents from family_members
tup4=family_members[:3]
tup5=family_members[3:]
print(tup4,tup5)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("apple","orange","cherry")
vegitables=("carrot","beatroot","tomato")
animal_products=("milk","cheese")
food_stuff_tp=fruits+vegitables+animal_products
print(food_stuff_tp)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
list1=list(food_stuff_tp)
print(list1)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
n=len(list1)
print(n//2)
print(list1[n//2])
#Slice out the first three items and the last three items from food_staff_lt list
print(list[:3])
print(list[:-3])
#Delete the food_staff_tp tuple completely
del food_stuff_tp
"""Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)