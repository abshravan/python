# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
#Insert multiple IT companies at once to the set it_companies
it_companies.update(["Qburst","UST","Fitgirl"])
#Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print(it_companies)
#What is the difference between remove and discard
it_companies.discard("gst")
print(it_companies)
#Exercises: Level 2
#Join A and B
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3674521289.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1293947566.
print(A.union(B))
print(B.union(A))
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
del B

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age1=set(age)
print(len(age),len(age1))
#Explain the difference between the following data types: string, list, tuple and set
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str1="I am a teacher and I love to inspire and teach people"
str2=str1.split(" ")
str2=set(str2)
print(str2)
print(len(str2))