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
your_age=int(input("Enter your age:"))
my_age=int(input("Enter my age"))
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
num_1=int(input("entr the first number"))
num_2=int(input("enter the second number"))
if num_1>num_2:
    print(str(num_1)+" is greater than "+str(num_2))
elif num_1<num_2:
    print(str(num_1)+" is less than "+str(num_2))
else:
    print(str(num_1)+" is equal to "+str(num_2))
