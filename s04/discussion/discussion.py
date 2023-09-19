 #Lists, Dictionaries, Functions and Classes


# Lists - they can contain collection of data

name = ["John", "Paul","Mrinal","Messi"] # String list 
programs=['developer career','pi-shape','short courses']
duration=[260, 180, 20] # Number list
truth_values=[True, False, True , True , False] # Boolean list
# lists can contain elements of diff data types but this is not recommended
# len method for size 
print(len(programs))
# for targetting values in the list
print(programs[0])
# mini activity
students=["Mrinal","Messi","Mascherano","Mauguire","Mendy"]
grades=[99,100,89,9,45]
count=0
for student in students:  # better if you use while here
	print(f"{student} scored {grades[count]}")
	count+=1
# to append we use append function and to delete we use del function
name.append("Naby")
print(name)
del name[-1]
print(name)
# membership check using "in"
print("Naby" in name)
print("Paul" in name)
# sort() method sorts list alphanumerically, ascending by default
name.sort()
print(name)
# clear() method empties the content of the list
# to copy a list to another list, 
#we use this method because names=name will just add another pointer to the data rather than copy the data
Names=list(name)
print(Names)





# Dictionaries 
# they store data in key:value pairs
person1={
	"name":"Brandon",
	"age":28,
	"occupation":"student",
	"isEnrolled":True,
	"subjects":["python","SQL","Django"]   # list inside dictionary
}

print(len(person1))
print(person1["name"]) 
#keys() method will return a list of all the keys in the dictionary
print("\n\n")
print(person1.keys())
#values() method will return a list of all the values in the dictionary
print("\n\n")
print(person1.values())
#items() method will return each item in dictionary ie key-value pair in a list
print("\n\n")
print(person1.items())
#update() method will add key-value pairs putting a new index in the dictionary
person1["nationality"]='Nepalese'
person1.update({"fav_food":"momo"})
print("\n\n")
print(person1)
#you can delete using the pop() method of the del keyword
person1.pop("fav_food")
del person1["nationality"]
print("\n\n")
print(person1)
#clear method empties the dictionary
person2={
	"name":"jane"
}
person2.clear()
print(person2)
#Looping through dictionary
for key in person1:
	print(f"the value of the {key} is {person1[key]}")
#Nested Dictionaries
person3={
	"name":"Mrinal",
	"age":20,
	"occupation":"footballer",
	"isEnrolled":True,
	"subjects":["python","django","sql"]
}
clasRoom={
	"student1":person1,
	"student2":person3
}
print(clasRoom['student1']['name'])

# Mini Exercise

car={
	"brand":"tesla",
	"model":"X",
	"yearOfMake":2018,
	"color":"white"
}
print(f"I own a {car['brand']} {car['model']} and it was made in {car['yearOfMake']}.")   
# the quotation should be single ie '' for the literals





# FUNCTIONS IN PYTHON
# def <function name>(parameters)

#defining a function
def myGreeting():
	print('Hello User!')

#calling a function
myGreeting()

def greetUser(username):
	print(f"Hello, {username}!")

greetUser('Manav')  #these are arguments
greetUser('Lantho')

def addition(num1,num2):
	return num1+num2

sum=addition(15,15)
print(f"The sum is {sum}.")

#Lambda function- 
# it is a small anonymous function that can be used for callbacks,
# which can only be contained in one line and only performs one task ie one expression
# but can take more than one parameters
greeting=lambda person:f'hello {person}'

print(greeting('Elsa'))
print(greeting('Maradona'))

multiply=lambda a,b: a*b 
print(multiply(5,20))

# Mini Exercise
def square(n):
	return n*n

print(f"The square of 3 is {square(3)}.\n")





# CLASSES IN PYTHON
# they serve as blueprints to describe the concept of objects
# each ocject has characteristics(properties) and behaviors (methods)

class Car():  #capitalize first letter- convention
	#properties
	def __init__(self,brand,model,year_of_make):
		self.brand=brand #self pretends to the object that will be created later
		self.model=model
		self.year_of_make=year_of_make

		self.fuel="Gasoline"  #hardcoded info of the class
		self.fuel_level=0
	#method
	def fill_fuel(self): #self is always included in the methods
		print(f"Current fuel level: {self.fuel_level}")
		print('filling up the fuel tank...')
		self.fuel_level=100
		print(f"Current fuel level: {self.fuel_level}\n")
	# Mini Exercise
	def drive(self, distance):
		print(f'The car has driven {distance} kms.')
		print(f"The car's fuel level is {self.fuel_level - distance}.\n")

#intance is done by calling the class and providing the arguments
new_car=Car("Nissan","GT-R", 2019)

#displaying the attribute
print(f'My car is {new_car.brand} {new_car.model} and it was manufactured in {new_car.year_of_make}.')

new_car.fill_fuel()
# Mini Exercise
new_car.drive(300)
