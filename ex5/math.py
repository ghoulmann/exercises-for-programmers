# Simple Calculator
# Exercise 5
# Python solution (attempt 1)
# needs to be revised for constraints

# Manage input and datatype
first = raw_input("What is the first number? ")
num1 = int(first)
second = raw_input("What is the second number? ")
num2 = int(second)

# answers as strings
addition = str(num1 + num2)
subtraction = str(num1 - num2)
times = str(num1 * num2)
div = str(num1 / num2)

# function to reduce redundancy
def output(first, second, sign, name):
    print(first + " " + sign + " " + second + " = " + name)
    
# use function to produce suggested output
addition = output(first, second, "+", addition)
subtraction = output(first, second, "-", subtraction)
times = output(first, second, "*", times)
div = output(first, second, "/", div)

out = """
%s
%s
%s
%s
""" % (addition, subtraction, times, div)

print out 







