"""
    Python program to show use of 
    + operator for different purposes.
"""
print 1 + 2

# Concantenate two strings
print 'Franklin' + 'Kirimi'

# Product two numbers
print 3 * 4
# Repeat the String
print "Hell_yeah!..., " * 4

# ------------------------------------------------------------------------
# Python Program illustrate how
# to overload an binary + operator


class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("franklin_")
ob4 = A("Kirimi")

print ob1 + ob2
print(ob3 + ob4)


# ------------------------------------------------------------------------
# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class Complex:
    def __init(self, a, b):
        self.a = a
        self.o = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a, self.b


object_one = complex(1, 2)
object_two = complex(2, 3)


print 'Complex Object addition >> ', object_one + object_two
