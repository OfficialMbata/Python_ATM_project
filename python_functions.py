import os
os.system('cls' if os.name == 'nt' else 'clear')
import math
# what are functions?
# It is a small re-useable block of code that does one specific job

# Why do we use functions
#  for easy debugging
#  fast changes to code
#  safer(low risk)
#  smaller and clean codes
#  easy to read and understand

# sources of functions
# Built-in functions: they come with python. 
# Libraries:
# Standard python library: they are written by python team. we have to import them. E.g math, datetime, random
# External Library: written by community, other developers. we have to install them because they don't come with python, then import them. E.g Pandas, Matplotlib, Numpy
# User-defined functions: they are written by you. we just have to define them and then use them.

# How to choose between sources?
# Golden rule
# Before writing new code, always check if it already exists!
# check the Built-in Functions
# check the Libraries
# check with your team ---------> User-defined functions f(x)
# write your user-defined function f(x)

# How functions work (User defined functtion)
# function definition, declaration or description: here, you define the function or what the function does 
# def function_name():
#   body

# function call or execution: is how you use the function
# function_name()

# def greet():
#   print('hello')

# greet()

# functions: simple example
# def make_coffee():
#   print('start machine')
#   print('make coffee')
#   print('add milk')
#   print('enjoy it')

# print('wake up')
# print('start machine')
# print('make coffee')
# print('add milk')
# print('enjoy it')
# print('working for a while')
# make_coffee()

# Built-in function
# print(len('python'))

# function from library
# number = 4.2
# print(math.ceil(number))

# # user defined function
# def greet():
#   print('Hello')

# greet()

# PARAMETERS AND ARGUMENTS
# Parameters: are names used in function definition that describe what data the function expects
# Arguments: are actual values passed in a function call that are assigned to parameters


# def clean_name(name):
#   print(name.strip().lower())

# clean_name(' MariA  ')
# clean_name('KUMAR')

# PARAMETERS: LOCAL AND GLOBAL VARIABLES
# f = 2
# def multiple_two(x):
#   y = x * f
#   print(y)

# multiple_two(3)

# Global variable is a variable that is created outside the function and can be accessed anywhere.
# Local variable is a variable that is created inside the function and can be accessed only inside the function

# case_rule = 'lower'
# def clean_name(name):
#   cleaned = name.strip().lower()
#   if case_rule == 'lower':
#     cleaned = cleaned.lower()
#   print('Raw:', name)
#   print('cleaned:', cleaned)

# clean_name(' MariA  ')

# POSITIONAL & KEYWORD ARGUMENT
# Positional Arguments: are values pass to the function based on their order
# Keyword Arguments: are values pass to the function by the name of the parameter

# def clean_name(first_name, last_name, country = "n/a"):
#   first = first_name.strip().lower()
#   last = last_name.strip().lower()
#   full_name = first +' '+ last
#   print(full_name, 'from', country)

# clean_name(" MariA  ", 'SMITH ', 'Germany') # positional argument
# clean_name(first_name = " MariA  ", last_name = "SMITH ", country = "GERMANY") # keyword argument

# Mix Argument: contains both positional and keyword arguments
# RULE
# they always start with positional argument then keyword argument
# clean_name(" MariA  ", last_name = "SMITH ", country ="Germany") # mix argument
# Default parameters: are parameters that already has a value so if you don't pass anything in, python uses that value automatically
# RULE
# Parameter without a default value follows parameter with a default value
# clean_name("Kumar", "Suresh")

# *ARGS & **KWARGS
# Sometimes, you don't know how many arguments will be passed to your function. *args and **kwargs allow functions to accept a unknown number of arguments
# * -------> positional arguments
# ** ------> keyword arguments

# calculate the total of values
# def total(a, b):
#   print(a + b)

# total(1, 2)

# instead do this
# def total(*args):
#   print(type(args))
#   print(sum(args))

# total(1,2)
# total(1,2,3)
# total(1,2,3,4)
# total(1,2,3,4,5)
# total(1,2,3,4,5,6)

# When to use *args
# when you pass similar values
# Thry only work with positional argument

# They store data in tuples

# Create a user profile
# def create_user(**kwargs):
#   print(type(kwargs))
#   print(kwargs)

# create_user(first_name = "Mo",
#             last_name = "Salah",
#             age = 33,
#             country = 'Egypt')
# when to use kwargs
# when you pass different types of values
# they only work with keyword argument

# they store values in dictionaries

# RETURN
# f = 2
# def multiple_two(x):
#   y = x * f
#   return y

# z = multiple_two(3)
# print(z)

# def clean_name(name):
#   if not name: # If the value is empty, convert it to None. Otherwise, clean it.
#     return None
#   else:
#     cleaned = name.strip().lower()
#     return cleaned

# cln_name = clean_name("")
# print(cln_name)

# If a function has no return statement, python returns None.
# A function can have multiple return statement.
# You can return multiple values seperated by commas.

# return the value both in lower and upper case.
# def clean_name(name):
#   lo_cleaned = name.strip().lower()
#   up_cleaned = name.strip().upper()
#   return lo_cleaned, up_cleaned

# cln_name = clean_name(" MariA  ")
# print(cln_name)

# Function Types: By purpose
# Action Function: it is designed to perform an operation in the system instead of returning values.

# Task:
# Store application log messages in a file whenever an event occurs
#with open opens the file safely and closes it automatically when done."a" appends data at the end of a file.

def write_log(message):
  with open(r"C:\Main\Python\app.log", "a") as file:
    file.write(message + "\n")
    
write_log("App Started") 

# Transformation function: it takes raw data, transforms it and returns processed data
# Task:
# Clean email addresses and splits them intostructured data (username and domain)

def clean_and_split_email(email):
  cl_email = email.strip().lower()
  username, domain = cl_email.split("@")
  return {
    "username": username,
    "domain": domain
  }

# print(clean_and_split_email('saRA@gmail.com'))

# Validation function: it validates a condition and returns a boolean result (True or False)
# Task:
# Checks whether the password meets the minimum requirement of 8 characters

def is_password_valid(password):
  return len(password) >= 8
# print(is_password_valid('123456'))
# print(is_password_valid('12345678'))

# checks whether an email has a basic valid format.

def is_email_valid(email):
 return "@" in email and "." in email

# print(is_email_valid("sara@gmailcom"))
# print(is_email_valid("saragmail.com"))
# print(is_email_valid("sara@gmail.com"))
# print(is_email_valid("saragmailcom"))

# Orchestrator Function: it controls program flow by calling other functions in correct order. It focuses on co-ordination and workflow.

# project
# Receive an email from the user.
# validate the email.
# if it is valid, log an error in the file.
# if it is valid, clean and structure the email.
# log each step of the program

def process_user_email(email):
  write_log("App Started")
  # we check if its valid
  if not is_email_valid:  # if it is not valid
    write_log(f"Invalid Email received: {email}")
  # if it is valid, we clean it and store structure in email
  else:
    clean_email = clean_and_split_email(email)
    write_log(f"Processed Email: {clean_email}")
  write_log(f"App Stopped")

# # we recieve user email
email = input("Enter user email: ")
process_user_email(email)

# 8x Habits: writing functions(function styling)
# Bad style
# def DiscPrint(p, r):
#   print("Calculating discount")
#   p = p - (p * r/100)
#   print(p)

# DiscPrint(80, 20)

# RULES:
# use snake_case for Function names: write function names in lowercase and seperate words with underscores.
# use clear descriptive Function Names: Describe what your function does, start with a verb, use full words, and avoid abbreviations
# Parameter names should describe their values: use full, meaningful words, avoid abbreviation and single letters
# Always describe functions using Docstring: help teammates understand your code, help future you understand the logic. Docstringis a short text on the first line inside the function that explains what the function does.
# Replace Prints with Return to send data back to the program
# Don't change parameter values directly, instead craete local variables for any processing.
# return one-line expression directly: put simple calculations directly inside the return statement instead of storing rhem in extra variables.(not a must follow though). e.g return price - (price * rate/100)
# use data type hints: always add type hints to parameters and return to make the function easier to understand
# explain Args & Return in Docstring: Always describe what goes in and what comes out of the function in the docstring

# Correction
# def calculate_discount(price: float, rate: float)-> float:
#   """
#   Calculate the final price after applying a discount.
#   Args:
#     price (float): Original Product Price.
#     rate (float): Discount rate as numbers (e.g 20 for 20%).
#   Returns:
#     final_price (float): Final price after applying discount.
#  """
#   final_price = price - (price * rate/100)
#   return(final_price)

# print(calculate_discount(500.00, 20))

# LAMBDA FUNCTION
# multiple = lambda x: x * 2
# print(multiple(4))

# add = lambda x, y: x + y
# print(add(1, 2))

# Note
# when  a lambda has two parameters, you must pass two values when calling it.
# a lambda can contain any expression, including conditions

# check = lambda i: i in "python"
# print(check('n'))

# LAMBDA + MAP
# Task: prices are stored as messy strings and needs cleaning to floats
# prices = ['$12.50', '$9.99', '$100.00']

# print(list(map(lambda p: float(p.replace('$', '')), prices)))

# steps
# Data transformation
# Put it in lambda
# Map the function to iterator to manipulate the data

# LAMBDA + FILTER
# Task: Remove all prices lower than 100
# prices = [120, 30, 300, 80]

# print(list(filter(lambda p: p >= 100, prices)))

# Keep only students with score higher than 70
# students = [
#   ['Maria', 85],
#   ['Kumar', 90],
#   ['Max', 60]
# ]

# print(list(filter(lambda row: row[1] > 70, students)))
# students[0][1] > 70


# Task: keep only students with names starting with "M"
# print(list(filter(lambda row: row[0].startswith('M'), students)))


# LAMBDA function
# create quick and custom logic
# One-line function
# assist others, e.g map(), filter(), sort().
# adds dynamic and flexibility