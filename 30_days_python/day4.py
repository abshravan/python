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
#level2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages[0],ages[len(ages)-1])
#Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[len(ages)-1])
print(ages)
#Find the median age (one middle item or two middle items divided by two)
median_age=ages[n//2]
print(median_age)
#Find the average age (sum of all items divided by their number )
average_age=sum(ages)/n
print(average_age)
#Find the range of the ages (max minus min)
range_age=ages[len(ages)-1]-ages[0]
#Compare the value of (min - average) and (max - average), use abs() method
#abs is absolute value
n1=abs(ages[0]-average_age)
n2=abs(ages[len(ages)-1]-average_age)
print(n1,n2)
#second question
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries)
#Find the middle country(ies) in the countries list
print(countries[n//2])
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
coun1=countries[:n//2]
coun2=countries[:-(n//2)]
print(coun1)
print("\n")
print(coun2)
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
lastlist=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic=lastlist[3:]
print(scandic)
lastlist.pop(0)
lastlist.pop(1)
lastlist.pop(2)
print(lastlist)