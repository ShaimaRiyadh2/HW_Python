'''
 explan of the differences between instance methods, class methods, and static methods in Python:

1. Instance Methods:

   - Definition: Instance methods are bound to an instance of a class and can access and 
   modify the instance's attributes. They are the most common type of methods in Python classes.
   - Access: Instance methods have access to the instance itself via the self parameter, 
   allowing them to manipulate instance-specific data.
   - Usage: Instance methods are used to perform actions or operations that are specific
   to individual instances of a class. They can access and modify instance variables and call other instance methods.
   - Example: Methods like init (the constructor), get, set, or any other behavior that
   operates on instance-specific data are typically implemented as instance methods.
   
1. Class Methods:

   - Definition: Class methods are bound to the class itself rather than an instance. 
   They can access and modify class-level attributes and perform operations that are related to the class as a whole.
   - Access: Class methods have access to the class itself via the cls parameter,
   allowing them to access class-level data and call other class methods.
   - Usage: Class methods are often used when you need to perform an action that involves the class but doesn't 
   require access to specific instance data. They are commonly used for alternative constructors, factory methods,
   or for performing operations that affect the class as a whole.
   - Example: Methods like from_string, from_file, or any other behavior that creates instances of 
   the class or operates on class-level data are typically implemented as class methods.

1. Static Methods:

   - Definition: Static methods are independent of both the class and its instances. They are not bound to
   any specific instance or class and do not have access to instance or class attributes.
   - Access: Static methods do not require any special parameters like self or cls and cannot access instance 
   or class data directly.
   - Usage: Static methods are used when a method doesn't depend on instance or class
   state and doesn't need access to instance or class attributes. They are often used for utility functions
   that are related to the class but do not require access to instance-specific or class-specific data.
   - Example: Utility methods that perform generic calculations, formatting functions, or any behavior 
   that doesn't rely on instance or class data are typically implemented as static methods.

In summary, instance methods are used for actions specific to individual instances and have access to 
instance data, class methods are used for actions related to the class as a whole and have access to
class-level data, while static methods are independent of instances and classes and don't have access to
instance or class attributes.
'''
#Example include instance methods, class methods, and static methods
class MathUtils:
    # Instance Method
    def add(self, a, b):
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        return a * b

    # Static Method
    @staticmethod
    def subtract(a, b):
        return a - b

# Creating an object of the MathUtils class
math_obj = MathUtils()

# Calling the instance method
result1 = math_obj.add(5, 3)
print("Result of instance method:", result1)
# Output: Result of instance method: 8

# Calling the class method
result2 = MathUtils.multiply(4, 6)
print("Result of class method:", result2)
# Output: Result of class method: 24

# Calling the static method
result3 = MathUtils.subtract(10, 7)
print("Result of static method:", result3)
# Output: Result of static method: 3