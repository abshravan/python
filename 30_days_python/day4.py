#Declare an empty list
list=[]
#Declare a list with more than 5 items
list1=[1,3,4,6,7,8,2]
#Find the length of your list
n=len(list1)
print(n)
#Get the first item, the middle item and the last item of the list
print(list1[0],list1[n//2],list1[n-1])
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
list2=["shravan",22,180.4,"single","kollam"]
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
list3=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#Print the list using print()
print(list3, list2 ,list1)
#Print the number of companies in the list
print(len(list3))
#Print the first, middle and last company
print(list3[0],list3[n//2],list3[n-1])
#Print the list after modifying one of the companies
list3.append("meta")
print(list3)