#Exercises: Level 1
"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
age=int(input("Enter your age:"))
if age<=17:
    n1=18-age
    print("you need "+str(n1)+" years to drive")
else :
    print("You are old enough to drive")

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
Enter your age: 30
You are 5 years older than me.
"""
your_age=int(input("Enter your age: "))
my_age=int(input("Enter my age : "))
if my_age<your_age:
    n2=your_age-my_age
    print("you are "+str(n2)+" years older than me")
elif my_age>your_age:
    n3=my_age-your_age
    print("you are "+str(n3)+" years younger than me")
else:
    print("we are same age")
"""
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
num_1=int(input("enter the first number "))
num_2=int(input("enter the second number "))
if num_1>num_2:
    print(str(num_1)+" is greater than "+str(num_2))
elif num_1<num_2:
    print(str(num_1)+" is less than "+str(num_2))
else:
    print(str(num_1)+" is equal to "+str(num_2))
"""    
### Exercises: Level 2
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
score=int(input("Enter the grade"))
if score<=100 and score>=80:
    print("You got A grade")
elif score>100:
    print("Invalid grade")
elif score<80 and score>=70:
    print("You got B grade")
elif score<70 and score>=60:
    print("You got C grade")
elif score<60 and score>=50:
    print("You got D grade")
else:
    print("You got F grade")
"""
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
month=input("Enter the month ")
if month=="September" or month=="October" or month=="November":
    print("The season is Autumn")
elif month=="December" or month=="January" or month=="February":
    print("The season is Winter")
elif month=="March" or month=="April" or month=="May":
    print("The season is Spring")
elif month=="June" or month=="July" or month=="August":
    print("The season is Summer")
else:
    print("Invalid month")
"""
The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("enter the fruit name")
flag=new_fruit in fruits
if flag ==True:
    print("Fruit already exist")
else:
    fruits.append(new_fruit)
print(fruits)
