1. __str__()
Purpose: Controls how an object is displayed when we print it.


class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"Laptop: {self.brand}, Price: {self.price}"

l2 = Laptop("Dell", 50000)
print(l2)

# Output:
Laptop: Dell, Price: 50000

-------x------x----

2. Instance method
Uses self → works with one specific object.


class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name)

Here:
self refers to s1
It accesses that object's data.

------x-----x------

3. Class method
Uses cls → works with the entire class.


class Bank:
    bank_name = "ABC"

    @classmethod
    def change_name(cls, new_name):
        cls.bank_name = new_name

Bank.change_name("XYZ")

print(Bank.bank_name)
    

Output:
XYZ

------x----x----

4. Static method
Needs neither self nor cls.


class Math:

    @staticmethod
    def square(n):
        return n * n

print(Math.square(5))
    

Output:
25

s1 = Student("Yash")
s1.introduce()
