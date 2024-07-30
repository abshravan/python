# exersize 3
age=int(22)
height=float(180.4)
z1=complex(2,-2) #declaring a complex number
#area of a triangle
base= int(input("enter the base"))
height=int(input("enter the height"))
area_of_triangle=0.5*base*height
print(area_of_triangle)
#perimeter of a triangle
a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
perimeter_of_triangle=a+b+c
print("perimeter of triangle is ",perimeter_of_triangle)

d=int(input("enter the length"))
e=int(input("enter the width"))
area_of_rectangle=d*e
print("area of rectangle is ",area_of_rectangle)
perimeter_of_rectangle=2*(d+e)
print("perimeter of rectangle is ",perimeter_of_rectangle)

radius=int(input("enter the radius"))
area_of_circle=3.14*radius**2
print("area of circle is ",area_of_circle)
circum_of_circle=2*3.14*radius
print("circumference of circle is ",circum_of_circle)
#cordinate program
x1=2
x2=6
y1=2
y2=10
slop=(y2-y1)-(x2-x1)
eucliden_distance=((x2-x1)**2+(y2-y1)**2)**1/2
print("the slope is:",slop ,"the distance is :",eucliden_distance)
#task 8 and 10 are skipped

x=int(input("enter the value of x"))
y=(x**2)+(6*x)+9
print(y)
str1="python"
str2="dragon"
print(len(str1)>len(str2))
str3="on"
print(str3 in str1 and str3 in str2)
str4="I hope this course is not full of jargon"
str5="jargon"
print(str5 in str4)
str1_len=len(str1)
print(float(str1_len))
print(str(str1_len))

n1=int(input("enter the first number"))
if n1%2==0:
    print("even")
else:
    print("odd")

n2=7
n3=3
n4=n2//n3
n5=n2/n3
print(n4,n5)
print(int(n4))

print(type("10"),type(10))
print("9.8"==int(10))

hours=input("enter the number of hours" )
pay=input('enter the pay per hours')
weekly_earning=int(hours)*int(pay)
print(weekly_earning)

number_of_years=int(input("enter the number of years"))
seconds=number_of_years*365*24*60*60
print("you live for :",seconds)

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

