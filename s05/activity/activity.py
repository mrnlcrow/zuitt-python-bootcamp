# question in drive, link in google chat
from abc import ABC, abstractclassmethod

# 1
class Animal(ABC):
	@abstractclassmethod
	def eat(self,food):
		pass

	def make_sound(self):
		pass

# 2
class Cat(Animal):
	# Properties
	def __init__(self,name,breed,age):
		super().__init__()
		self.name=name
		self.breed=breed
		self.age=age
	# Methods
	# i) Setter
	def set_name(self,dummy):
		self.name=dummy
	def set_breed(self,dummy):
		self.breed=dummy
	def set_age(self,dummy):
		self.age=dummy
	# ii) Getters
	def get_name(self):
		print(f'The name of the cat is {self.name}')
	def get_breed(self):
		print(f'The name of the cat is {self.breed}')
	def get_age(self):
		print(f'The name of the cat is {self.age}')

	# iii) abstract methods
	def eat(self,food):
		print(f'Serve me {food}')

	def make_sound(self):
		print(f'Miaow! Nyaw! Nyaaaaa!')

	# iv) call function
	def call(self):
		print(f'{self.name}, come on!')



class Dog(Animal):
	def __init__(self,name,breed,age):
		super().__init__()
		self.name=name
		self.breed=breed
		self.age=age

	# Methods
	# i) Setter
	def set_name(self,dummy):
		self.name=dummy
	def set_breed(self,dummy):
		self.breed=dummy
	def set_age(self,dummy):
		self.age=dummy
	# ii) Getters
	def get_name(self):
		print(f'The name of the dog is {self.name}')
	def get_breed(self):
		print(f'The name of the dog is {self.breed}')
	def get_age(self):
		print(f'The name of the dog is {self.age}')

	# iii) abstract methods
	def eat(self,food):
		print(f'Eaten {food}')

	def make_sound(self):
		print(f'Bark! Woof! Arf!')

	# iv) call function
	def call(self):
		print(f'Here {self.name}!')


# TEST CASES:
dog1=Dog('Isis','Dalmatian',15)
dog1.eat('Steak')
dog1.make_sound()
dog1.call()

cat1=Cat('Puss','Persian',4)
cat1.eat('Tuna')
cat1.make_sound()
cat1.call()
