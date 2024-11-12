# Structure of the lambda:
#   lambda args : expression


# Basic "add" example (two args)
adding = lambda m, n: m + n
print(adding(5, 6))  # that prints 11

# the same idea with a normal function
def adding_not_lambda(m, n):
    return m + n
print(adding_not_lambda(5,6))  # that also prints 11


# Basic "square" example (only one args)
square = lambda m: m ** 2
print(square(3))  # that prints 9


# Using a lambda in a list
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # the lambda function defined inline
squared_numbers = list(map(square, numbers))  # that's the same as before, but using the predefined lambda
print(squared_numbers)  # Output: [1, 4, 9, 16]  (any option returns that)
