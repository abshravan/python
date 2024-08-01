#Create an empty dictionary called dog
dog={}
#Add name, color, breed, legs, age to the dog dictionary
dog={"name":"browny","color":"brown","breed":"nadan","leg":4,"age":2}
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={"first_name":"shravan","last_name":"krishna","gender":"male","age":22,"marital_status":"single","skills":["python","html","css"],"country":"india","city":"kollam","address":{"housename":"retnayalam","place":"kulamada","pincode":691574
}}
print(student)
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))
#Modify the skills values by adding one or two skills
student["skills"]=["python","html","css","java","c"]
#Get the dictionary keys as a list
print(student.keys())
#Get the dictionary values as a list
print(student.values())
#Change the dictionary to a list of tuples using items() method
print(student.items())
#Delete one of the items in the dictionary
print(student.pop("age"))
print(student)
#Delete one of the dictionaries
del student