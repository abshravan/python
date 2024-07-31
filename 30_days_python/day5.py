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
