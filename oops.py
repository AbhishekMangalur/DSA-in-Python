# classes and objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}" )
        
obj = Car("Maruti", "Alto")
obj.display()


# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car started")
        
c = Car()
c.start()


# Encapsulation
class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
        
    def deposite(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
b = Bank(12345, 1000)
b.deposite(500)
print(b.get_balance())


# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speak(self):
        print("Bark")
        
d = Dog()
d.speak()


# Polymorphism
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speak(self):
        print("Bark")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
        
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()