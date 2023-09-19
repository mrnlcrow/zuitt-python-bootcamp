#input() function allowa to give input in python
username=input("Please enter your name:\n")
print(f"Hello {username}! YOU WILL BEAT YOUR ACL INJURY!")
num1=input("Enter 1st number: ")	
num2=input("Enter 2nd number: ")
print(f"The sum is {num1+num2}.")
num3=int(input("\n\nEnter 1st number: "))	
num4=int(input("Enter 2nd number: "))
print(f"The sum is {num3+num4}.")

# Control Structures
# Selection Control Structures
#if..else
test_num=30
if test_num>=25:
	print("test passed!")
else:
	print("failed!")
#it is elif NOT elseif
# Mini Exercise 1:
n=int(input("Enter an integer: \n"))
if (n % 5 == 0 and n%3==0 ):
	print("The number is divisible by both 3 and 5.")
elif (n%5==0):
	print("The number is divisible by 5 only.")
elif(n%3==0):
	print("The number is divisible by 3 only.")
else:
	print("The number is not dividible by neither 3 nor 5.")


# Repitition Control Structure
#while
i=1
while i<=5:
	print(f"current count {i}") #the line is changed automatically
	i+=1
#for loop
for x in range(6):
	print(f"the current value is {x}.")


fruits=["apple","banana","watermelon"] #this is a list
for fruit in fruits:
	print(fruit)

for y in range(6,10): #closed bracket in 6 but open in 10
	print(y)

for z in range(6,20,2): #the third input specifies the interval
	print(z)

#break is same as C
#UNARY OPERATORS DONT WORK IN PYTHON
#CONTINUE same as in c
