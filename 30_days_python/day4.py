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
list3.insert(2,"ust")
print(list3)
#Add an IT company to it
list3.append("meta")
#Insert an IT company in the middle of the companies list
list3.insert(n//2,"qburst")
#Change one of the it companies names to uppercase (IBM excluded!)
list3[1]=list3[1].upper()
print(list3)
#Join the it_companies with a string '#;  '
#print("#; ".join(list3))
#Check if a certain company exists in the it_companies list.
print("qburst" in list3)
#Sort the list using sort() method
list3.sort()
print(list3)
#Reverse the list in descending order using reverse() method
list3.reverse()
print(list3)
#Slice out the first 3 companies from the list
print(list3[3:])
#Slice out the last 3 companies from the list
print(list3[:3])
#Slice out the middle IT company or companies from the list
print(list3[n//2])
#Remove the first IT company from the list
list3.pop(1)
print(list3)
#Remove the middle IT company or companies from the list
list3.pop(n//2)
print(list3)
#Remove the last IT company from the lis
list3.pop(n-1)
print(list3)
#Remove all IT companies from the list
list3.clear()
#Destroy the IT companies list
del list3
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end+back_end)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=front_end+back_end
print(full_stack)
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)