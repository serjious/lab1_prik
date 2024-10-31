from abc import ABC, abstractmethod


class Movable(ABC):
	@abstractmethod
	def go(self):
		pass

class Flyable(Movable):
	@abstractmethod
	def fly(self):
		pass

class Car(Movable):
	def __init__(self, brand : str, power : int):
		self.brand = brand 
		self.power = power
	def go(self):
		print("the car is driving")

class Bus(Car):
	def __init__(self, brand : str, power : int, num_of_pass : int):
		Car.__init__(self, brand, power)
		self.num_of_pass = num_of_pass
	def go(self):
		print("the bus is driving")


