#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1,str2,str3,str4="Thrirty ","Days ","Of ","Python "
print(str1+str2+str3+str4)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
str5,str6,str7="Coding ","For ","All "
print(str5+str6+str7)
#Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For  All"
#Declare a variable named company and assign it to an initial value "Coding For All".
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize(),company.title(),company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company[7:1])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"))
#Change Python for All to Python for Everyone using the replace method or other methods.
print(company.replace("All","Everyone"))
#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str8="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str8.split(","))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What is the character at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(company[0:1],company[7:8],company[11:12])
#Create an acronym or an abbreviation for the name 'Coding For All'.
str_new="Coding For All"
print(str_new[0:1],str_new[7:8],str_new[11:12])
#Use index to determine the position of the first occurrence of C in Coding For All.
print(str_new.index("C"))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(str_new.index("F"))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
str_new2="Coding For All People"
print(str_new2.rfind("l"))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new="You cannot end a sentence with because because because is a conjunction"
print(new.index("because"))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new.rindex("because"))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new2="You cannot end a sentence with because because because is a conjunction"
print(len(new2),new2.rfind("because"))
print(new2[31:54])
#You cannot end a sentence with because because because is a conjunction
print(new2.find("because"))
#Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
#Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
new3="  Coding For All   "
print(new3.strip())
'''
#Which one of the following variables return True when we use the method isidentifier():30DaysOfPython thirty_days_of_python
print(isidentifier("30DaysOfPython"))
print(isidentifier("thirty_days_of_python"))
'''
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list1=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" #".join(list1))
#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
#Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity\nShravan\t22\tIndia\tKollam")
#Use the string formatting method to display the follwing lines.
radius = 10
area = 3.14 * radius ** 2
print('Area of the circle with radius {} is {} meters sq'.format(radius, area))
#make the following using string formatting methods
