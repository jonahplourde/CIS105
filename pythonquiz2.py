#Submit a URL link to your completed repository ON GITHUB on Moodle. 

#variables: show an example of variable assignment and usage. Be sure to print the variable to demonstrate its value.
favorite_food = input("What is your favorite food? ")
print("Your favorite food is:", favorite_food)

#data types: demonstrate at least three different data types (e.g., integer, string, list) and print their types using the type() function.
print(type(favorite_food))  # string
age = 21  # integer
print(type(age))  # integer
hobbies = ["reading", "coding", "hiking"]  # list
print(type(hobbies))  # list


#functions: define a simple function that takes an argument and returns a value. Call the function and print the result.
def greet(name):
	return f"Hello, {name}!"

greeting = greet("Alice")
print(greeting)

#classes: create a simple class with an __init__ method and one other method. Instantiate the class and call the method, printing the result.
class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
