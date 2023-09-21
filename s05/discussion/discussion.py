#	                                                    OOP concept in Python
# 4 pillars: Encapsulation, Inheritance, Polymorphism & Abstraction

# Recalling Python Class
class sampleClass():
	# The class constructor or intialization method is called by Python every time an instance of the class is created
	# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
	def __init__(self,year):
		self.year=year

	# methods are functions inside a class	
	def show_year(self):
		print(f"The year is: {self.year}")

myObj=sampleClass(2023)

print(myObj.year)
myObj.show_year()

#                                                        PILLAR : ENCAPSULATION
# Encapsulation is a mechanism of wrapping the attributes and code acting on the methods together as a single unit

# In encapsulation, the attributes of a class will be hidden from
# other classes, and can be accessed only through the methods of
# their current class. Therefore, it is also known as data hiding.

# To achieve encapsulation −
# * Declare the attributes of a class.
# * Provide getter and setter methods to modify and view the attributes values.

# Why encapsulation?
# The fields of a class can be made read-only or write-only.
# A class can have total control over what is stored in its fields.
class Person():
	def __init__(self):
		# The prefix underscore is used as a warning for developers that
		# means: "Please be careful about this attribute or method, don’t use
		# it outside of the declared Class"
		self._name='Hillary'
		self._age=0

	# setter method- set the value of _name to the variable name
	def set_name(self,name):
		self._name=name

	# getter method- to get the value of name
	def get_name(self):
		print(f'Name of Person: {self._name}')

	# answer of Mini Exercise 1
	def set_age(self,age):
		self._age=age
	def get_age(self):
		print(f'Age of Person: {self._age}')

p1=Person()

#print(p1.name)  ->displays error
p1.get_name()
p1.set_name('Mrinal')
p1.get_name()

# Mini Exercise 1
# Add another protected attribute called age and create the necessary getter and setter methods
# Test Cases:
p1.set_age(38)
p1.get_age()


#                                                         PILLAR : INHERITANCE
# The transfer of the characteristics of a parent class to child classes that are derived from it.
# An example of this is an employee and a person. An employee is a person with additional attributes and methods
# To create an inherited class, in the ClassName definition, add the parent class as the argument
# Syntax: class ChildClassName(ParentClassName)
class Employee(Person): #parent-class: person
	def __init__(self, employeeId):
		# super() can be used to invoke immediate parent class constructor
		super().__init__() 
		# attribute unique to the child class ie Employee
		self._employeeId=employeeId

	def get_employeeId(self):
		print(f'The Employee ID is {self._employeeId}')

	def set_employeeId(self,employeeId):
		self._employeeId=employeeId

	def get_details(self):
		print(f'{self._employeeId} belongs to {self._name}')

employee1=Employee('em-001')
employee1.get_details()
employee1.set_name('Messi')
employee1.set_age(36)
employee1.get_details()

# Mini exercise 2
# 1. Create a new class called Student that inherits Person with the additional attributes and methods
# attributes: Student No, Course, Year Level
# methods: 
#   get_detail: prints the output "<Student name> is currently in year <year level> taking up <Course>"
#   necessary getters and setters
class Student(Person):
	def __init__(self,studentNo,courseNo,yearLevel):
		super().__init__()
		self.studentNo=studentNo
		self.courseNo=courseNo
		self.yearLevel=yearLevel

	def get_details(self):
		print(f'{self._name} is currently in year {self.yearLevel} taking up {self.courseNo}.')

	#necessary getters and setters
	def get_studentNo(self):
		print(f'The Student Number is {self.studentNo}')

	def set_studentNo(self,studentNumber):
		self.studentNo=studentNumber

	def get_courseNo(self):
		print(f'The Course Number is {self.courseNo}')

	def set_courseNo(self,courseNumber):
		self.courseNo=courseNumber

	def get_yearLevel(self):
		print(f'The Employee ID is {self._employeeId}')

	def set_yearLevel(self,level):
		self.yearLevel=level

# Test cases:
student1 = Student("stdt-001", "Computer Science", 1)
student1.set_name("Brandon Smith")
student1.set_age(18)
student1.get_details()




#                                                         PILLAR : POLYMORPHISM 
# A child class inherits all the methods from the parent
# class. However, in some situations, the method inherited from the parent
# class doesn’t quite fit into the child class. In such cases, you will have
# to re-implement method in the child class.

# There are different methods to use polymorphism in Python. You can use
# different function, class methods or objects to define polymorphism. So,
# let’s move ahead and have a look at each of these methods in detail.

# Functions and objects
# A function can be created that can take any object, allowing for polymorphism.

class Admin():
	def is_admin(self):
		print(True)

	def user_type(self):
		print('Admin User')

class Customer():
	def is_admin(self):
		print(False)

	def user_type(self):
		print('Regular User')

def test_function(obj):
	obj.is_admin()
	obj.user_type()

user_admin = Admin()
user_customer= Customer()

test_function(user_admin)
test_function(user_customer)

# Polymorphism with Classes
class TeamLead():
	def occupation(self):
		print('Team Lead')

	def has_Auth(self):
		print(True)

class TeamMember():
	def occupation(self):
		print('Team Member')

	def has_Auth(self):
		print(False)

tl1=TeamLead()
tm1=TeamMember()
#hence, this looping will be easier to go through 9-10 or alot of classes
for person in (tl1,tm1):  #'person' is a variable that we will store the object in i.e. in run 1, person=tl1=tl1.occupation()
	person.occupation()


# Polymorphism with Inheritance
class Zuitt():
	def tracks(self):
		print('We are currently offering 3 tracks(developer career, pi-shape career, and short courses)')

	def num_of_hours(self):
		print('Learn web dev in 360 hours!')

class DeveloperCareer(Zuitt):
	def num_of_hours(self):
		print('Learn web dev in 240 hours!')

class PiShapedCareer(Zuitt):
	def num_of_hours(self):
		print('Learn no-code app development in 140 hours!')

course1= DeveloperCareer()
course2=PiShapedCareer()

# this is polymorphism not inheritance
course1.num_of_hours()
course2.num_of_hours()



#                                                           PILLAR : ABSTRACTION
# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created 
# within any child classes built from the abstract class. 
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.
# Abstract classes are used to provide a common interface for different implementations for different classes.
# By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining 
# Abstract Base classes(ABC) and that module name is ABC

from abc import ABC, abstractclassmethod

class Polygon(ABC):
	@abstractclassmethod
	def printNumberOfSides(self):
		pass 

class Triangle(Polygon):
	def __init__(self):
		super().__init__()

	def printNumberOfSides(self):
		print('This polygon has 3 sides.')

class Pentagon(Polygon):
	def __init__(self):
		super().__init__()

	def printNumberOfSides(self):
		print('This polygon has 5 sides.')

shape1=Triangle()
shape2=Pentagon()

shape1.printNumberOfSides()
shape2.printNumberOfSides()