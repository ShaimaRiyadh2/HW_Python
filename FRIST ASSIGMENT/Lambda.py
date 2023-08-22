''' 
A lambda function, also known as an anonymous function,
is a function without a name. It is a way to create small, one-line functions on the fly without needing to 
define a separate named function.  
Lambda functions are commonly used in programming languages that 
support functional programming paradigms.
''' 

#Example 1: Sorting a list of tuples based on the second element:
students = [('Alice', 22), ('Bob', 19), ('Charlie', 21), ('Dave', 20)]
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
# Output: [('Bob', 19), ('Dave', 20), ('Charlie', 21), ('Alice', 22)]
'''
In this example, a lambda function is used as the key argument in 
the sorted() function. The lambda function lambda x: x[1] specifies that the sorting should
be based on the second element of each tuple.
As a result, the list of students is sorted based on their ages.
'''

#Example 3: Performing arithmetic operations:
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y

result1 = addition(5, 3)
result2 = subtraction(10, 4)

print(result1)  # Output: 8
print(result2)  # Output: 6

'''
In this example, lambda functions are used to define simple arithmetic operations.
The lambda function addition takes two arguments and returns their sum, while the
lambda function subtraction takes two arguments and returns their difference. 
The lambda functions are then called with specific values to perform addition
and subtraction operations.
'''