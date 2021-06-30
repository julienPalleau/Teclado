#########################################################
# Day1 Numbers, Arithmetic, and Printing to the Console #
#########################################################
# # Exercice 1 Print your age to the console.
# print("I am 45 years old")
# print("\n")
#
# # Exercice 2 Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
# print(f"27 years")
# print(f"{27*365} days")
# print(f"{27*52} weeks")
# print(f"{27*12} month")
# print("\n)")
#
# # Exercice 3 Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
# print(f"area of the circle with a radius of 5 units: {3.14*pow(5, 2)}")


#########################################################
# Day2 Strings, Variables, and Getting Input from Users #
#########################################################
# # Exercice 1 Ask the user for their name and age, assign theses values to two variables, and then print them.
# name, age = input("Veuillez saisir votre prenom et votre age separer par une virulge: ").split(",")
# print(f"votre prenom est {name}, et votre age est {age} ans")
#
# # Exercice 2 Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try
# # printing the variable before and after you reuse the name.
# x = 5
# x = 7
#
# print(x)
#
# # The value we get printed out is 7, not 5. However, if we print x before assigning a new value to this name, we get
# # the original value:
# x = 5
# print(x)
#
# x = 7
# # This is because Python is running our code top to bottom, so when we refer to x when calling print, we haven't yet
# # updated the value of x.


#####################################################
# Day3 Formatting Strings and Processing User Input #
#####################################################
# # Exercice 1 Using the variable below, print "Hello, world!".
# # greeting = "Hello, world"
# # You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.
# greeting = "Hello, world"
# greeting1 = greeting + " !"
# greeting2 = "{} !".format(greeting)
# greeting3 = f"{greeting} !"
# print(greeting1)
# print(greeting2)
# print(greeting3)

# # Exercice 2     Ask the user for their name, and then greet the user, using their name as part of the greeting.
# # The name should be in title case, and shouldn't be surrounded by any excess white space.
# #
# # For example, if the user enters "lewis ", your output should be something like this:
# # Hello, Lewis!
# name = input("Please enter your name: ").title().strip(" ")
# print(f"Hello, {name}")

# # Exercice 3 Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
# age = 29
# print(f"I am {str(age)}")

# # Exercice 4     Format and print the information below using string interpolation:
# #
# title = "Joker"
# director = "Todd Phillips"
# release_year = 2019
# #
# # The output should look like this:
# #
# # Joker (2019), directed by Todd Phillips
#
# print(f"{title} ({release_year}), directed by {director}")


#################################
# Day4 Basic Python Collections #
#################################
# Exercice 1 Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s
# name, the release year of the movie, and the movie’s budget.
from typing import List

movie = [("Reservoir Dogs",
          "Quentin Tarantino",
          "1992",
          "$1,600,000")
         ]

# # Exercice 2 Use the input function to gather information about another movie. You need a title, director’s name,
# # release year, and budget.
# title, director, year, budget = input("Please provied information about a movie, You need a title, director’s name, release year, and budget separated by , : ").split(",")
# print(f"Titre : {title}, Director: {director}, release year: {year}, Budget : {budget}")
#
# # Exercice 3 Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the
# # tuple you wrote in the movies list.
# newTuple = title, director, year, budget
# print(type(newTuple))
#
# # Exercice 4 Use an f-string to print the movie name and release year by accessing your new movie tuple.
# print(f"the movie name is {newTuple[0]} and its realease year is {newTuple[2]}")

# # Exercice 5 Add the new movie tuple to the movies collection using append
# # Exercice 6 Print both movies in the movies collection.
# title, director, year, budget = input("Please provied information about a movie, You need a title, director’s name, release year, and budget separated by , : ").split(",")
# newTuple = title, director, year, budget
# movie.append(newTuple)
# print(movie)
#
# # Exercice 7 Remove the first movie from movies. Use any method you like.
# movie.pop(0)
# print(movie)


##################################
# Day5 Conditionals and Booleans #
##################################
# # Exercice 1 Try to approximate the behaviour of the is operator using ==. Remember we have the id function for
# # finding the memory address for a given value, and we can compare memory addresses to check for identity.
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# print(id(a) == id(b))

# # Exercice 2 Try to use the is operator or the id function to investigate the difference between this:
# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# print(id(new_numbers))
# print(id(new_numbers))
# # And this:
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# # Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
# print(id(numbers))
# print(id(new_numbers))
#
# # Exercice 3 Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
# number = int(input("Saisissez un entier positif ou negatif ou nul: "))
# if number > 0:
#     print(f"Vous avez saisi un entier positif {number}")
# elif number < 0:
#     print(f"Vous avez saisi un entier negatif {number}")
# else:
#     print(f"Vous avez saisi un entier nul")

# # Exercice 4 Write a program to determine whether an employee is owed any overtime. You should ask the user how many
# # hours the employee worked this week, as well as the hourly wage for this employee.
# # If the employee worked more than 40 hours, you should print a message which says the employee is due some additional
# # pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked
# # over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
# # You can find our solutions to these exercises here.
# workedHours = int(input("How many hours did you work this week ? : "))
# hourlyWage = float(input("What is your hour wage ? : "))
# if workedHours > 40:
#     print(f"Cette semaine vous avez gagne: £{40*hourlyWage} + £{(workedHours - 40) * 0.1 * hourlyWage} de prime")
# else:
#     print(f"Cette semaine vous avez gagne: £{40*hourlyWage}")


##################
# Day6 For Loops #
##################
# # Exercice 1 Below we've provided a list of tuples, where each tuple contains details about an employee of a shop:
# # their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be
# # paid at the end of the week in a nice, readable format.
# #
# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]
#
# for employee in employees:
#     print(f"employee {employee[0]} is due £{employee[1]*employee[2]}")

# # Exercice 2 For the employees above, print out those who are earning an hourly wage above average.
# # Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees.
# # Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list
# # again and prints out only those who have an hourly wage above the calculated average.
# total_wage = total_employee = 0
# for employee in employees:
#     total_wage += employee[2]
#     total_employee += 1
#
# average_wage = total_wage/total_employee
# print(f"average wage is {average_wage}")
# for employee in employees:
#     if employee[2] > average_wage:
#         print(f"{employee[0]} earn more than average.")


###############################
# Day7 Split, Join and Slices #
###############################
# # Exercice 1 Ask the user to enter their given name and surname in response to a single prompt. Use split to extract
# # the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a
# # single given name and a single surname.
# name, surname = input("Veuillez saisir votre nom et prenom :").split(" ")
# print(f"Votre nom est {name}, et votre prenom est {surname}")

# # Exercice 2 Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you
# # can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
# list1 = [1, 2, 3, 4, 5]
# result = []
# for number in list1:
#     result.append(str(number))
#
# print(result)
# print("| ".join(result))
# print(", ".join(result))

# Exercice 3 Below you’ll find a short list of quotes:
#
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
print("Solution - 1")
for quote in quotes:
    print(quote[1:-1])

print("\nSolution - 2")
for quote in quotes:
    print(quote.strip("'"))

#
# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing,
# extract the text from each string, without these extra quote marks, and print each quote.
#
# You may also want to try a solution using strip.

#########
# Day16 #
#########
# # Exercice 1 Use the sort method to put the following list in alphabetical order with regards to the student's names.
# students = [
# 	{"name": "Hannah", "grade_average": 83},
# 	{"name": "Charlie", "grade_average": 91},
# 	{"name": "Peter", "grade_average": 85},
# 	{"name": "Rachel", "grade_average": 79},
# 	{"name": "Lauren", "grade_average": 92}
# ]
#
# students.sort(key=lambda student: student["name"])

# Exercice 2 Convert the following function to a lambda expression and assign it to a variable called exp.
# def exponentiate(base, exponent):
# 	return base ** exponent
#
# print(exponentiate(2, 4))
#
#
# exp = lambda base, exponent: base ** exponent
# print(exp(2, 5))

# Exercise 3 Print the fuction you created using a lambda expression in previous exercise. What is the name of
# the function that was created?
# print(exp(2, 5))

# ----------------------------------

# #########
# # Day17 #
# #########
# Exercice 1 Create a function that accepts any number of numbers as positional arguments and prints the sum of those
# numbers. Remember that we can use the sum function to add the values in an iterable.
# def testFunc(*args):
#     print(sum(args))
#
#
# testFunc(2, 4)

# Exercice 2 Create a function that accepts any number of positional and keyword arguments, and that prints them back
# to the user. Your output should indicate which values were provided as positional arguments, and which were provided
# as keyword arguments.
# def arg_printer(*args, **kwargs):
#     args = [repr(arg) for arg in args]
#     print(f"Positional arguments are: {', '.join(args)}")
#
#     kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
#     print(f"Keyword arguments are: {', '.join(kwargs)}")
#
#
# arg_printer(1, "blue", [1, 23, 3], height=184, key=lambda x: x ** 2)

# Exercice 3 Print the following dictionary using the format method and ** unpacking.
# country = {
#     "name": "Germany",
#     "population": "83 million",
#     "capital": "Berlin",
#     "currency": "Euro"
# }
#
# country_template = """Name: {name}
# Population: {population}
# Capital: {capital}
# Currency: {currency}"""
#
# print(country_template.format(**country))
