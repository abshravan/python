#Exercises:level 1
#Iterate 0 to 10 using for loop, do the same using while loop.
x=0
while x<=10:
    print(x)
    x=x+1
#Iterate 10 to 0 using for loop, do the same using while loop.
for j in range(0,11):
    print(j)


"""
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
for i in range (1,8):
    print("*"*i)


"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
for i in range(1,9):
    for j in range(1,9):
        print("#",end=" ")
    print()


"""
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for i in range(0,11):
    print(str(i)+"x"+str(i)+"="+str(i*i))


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(0,len(list)):
    print(list[i])


#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101):
    if i%2==0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,101):
    if i%2==1:
        print(i)
