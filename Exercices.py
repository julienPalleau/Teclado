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
# # Exercice 1 Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s
# # name, the release year of the movie, and the movie’s budget.
# from typing import List
#
# movie = [("Reservoir Dogs",
#           "Quentin Tarantino",
#           "1992",
#           "$1,600,000")
#          ]

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

# # Exercice 3 Below you’ll find a short list of quotes:
# quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
# ]
# print("Solution - 1")
# for quote in quotes:
#     print(quote[1:-1])
#
# print("\nSolution - 2")
# for quote in quotes:
#     print(quote.strip("'"))
#
# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing,
# extract the text from each string, without these extra quote marks, and print each quote.
#
# You may also want to try a solution using strip.


# # Exercice 4 Ask the user to enter a word, and then print out the length of the word. You should account for any excess
# # whitespace in the user’s input, so you’re going to have to process the string before you find its length.
# #
# # If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them
# # how many characters are in the text overall, and you can also provide them a word count.
# # word = input('Please enter a word you can try to put white space : ').strip()
# # print(len(word))
# sentence = input('Please enter a sentence : ').strip()
# print(f"Character count: {len(sentence)}")
# print(f"Word count: {len(sentence.split())}")

####################
# Day8 While loops #
####################
# # Exercice 1 Write a short guessing game program using a while loop. The user should be prompted to guess a number
# # between 1 and 100, and you should tell them whether their guess was too high or too low after each guess.
# # The loop should keeping running until the user guesses the number correctly.
# import random
#
# x = random.randint(1, 10)
# reponse = int(input("Devinez un nombre tirez au hasard entre 1 et 10 : "))
# print(x)
# while reponse != x:
#     if reponse < x:
#         print("your number is too low")
#     elif reponse > x:
#         print("your number is too high")
#     reponse = int(input("Essayez encore, devinez un nombre tirez au hasard entre 1 et 10 : "))
#
# print("Bravo vous avez trouve le nombre magique !!!")

# # Exercice 2 Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# # Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield
# # one character at a time.
# for x in "python":
#     if x == 'o':
#         continue
#
#     print(x)
#
# # Exercice 3 Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out
# # every prime number between 1 and 100.
# x = 1
# while x <= 100:
#     print(x)
#     x += 1
#
# for x in range(1, 101):
#     print(x)


####################
# Day9 While loops #
####################
# # Exercice 1 Below is some simple data about characters from BoJack Horseman:
# #
# main_characters = [
#     ("BoJack Horseman", "Will Arnett", "Horse"),
#     ("Princess Carolyn", "Amy Sedaris", "Cat"),
#     ("Diane Nguyen", "Alison Brie", "Human"),
#     ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
#     ("Todd Chavez", "Aaron Paul", "Human")
# ]
# # The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# # Write a for loop that uses destructuring so that you can print each tuple in the following format:
# # BoJack Horseman is a horse voiced by Will Arnet.
# # Note that you're going to have to change the species information to lowercase when you print it. If you need a
# # reminder on how to do this, we covered it in day 3 of the first week.
# for name, voice, play in main_characters:
#     print(f"{name} is a {play.lower()} by {voice}.")

# # Exercice 2 Unpack the following tuple into 4 variables:
# # ("John Smith", 11743, ("Computer Science", "Mathematics"))
# # The data represents a student's name, their student id number, and their major and minor disciplines in that order.
# student_name, id_num, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# print(student_name, id_num, major, minor)

# # Exercice3 Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a
# # list containing three items, and a tuples containing four items.
# first_is_a_list = [1, 2, 3]
# second_is_a_tuple = ('one', 'two', 'three', 'four')
#
# print(list(zip(first_is_a_list, second_is_a_tuple)))

######################
# Day10 Dictionaries #
######################
# # Exercice 1 Below is a tuple describing an album:
# album = {
# 	"title": "The Dark Side of the Moon",
# 	"artist": "Pink Floyd",
# 	"year": 1973,
# 	"tracks": (
# 		"Speak to Me",
# 		"Breathe",
# 		"On the Run",
# 		"Time",
# 		"The Great Gig in the Sky",
# 		"Money",
# 		"Us and Them",
# 		"Any Colour You Like",
# 		"Brain Damage",
# 		"Eclipse"
# 	)
# }
#
# # Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another tuple containing the track list.
# # Convert this outer tuple to a dictionary with four keys.
# album = {
#  	"title": "The Dark Side of the Moon",
#  	"artist": "Pink Floyd",
#  	"year": 1973,
#  	"tracks": (
#  		"Speak to Me",
#  		"Breathe",
#  		"On the Run",
#  		"Time",
#  		"The Great Gig in the Sky",
#  		"Money",
#  		"Us and Them",
#  		"Any Colour You Like",
#  		"Brain Damage",
#  		"Eclipse"
#  	)
# }
# dic = {}
# dic.update(album)
# print(dic)
#
#
# # Exercice 2  Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you
# # should print the name of the key, and then the value alongside it.
# for key, value in dic.items():
#     print(f"key: {key}, value: {value}")
#
# # Exercice 3 Delete the track list and year of release from the dictionary you created. Once you've done this, add a new
# # key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st,
# # 1973.
# del dic["tracks"]
# dic['date_of_release'] = 'March 1st, 1973'
#
# # Exercice 4 Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError.
# # Once you've tried this, repeat the step using the get method to prevent the exception being raised.
# print(dic.get("tracks", "No key tracks"))
#
# print(dic)


#############
# Day11 Set #
#############
# # Exercice 1 Create an empty set and assign it to a variable.
# empty_set = set()
# print(type(empty_set))
#
# # Exercice 2 Add three items to your empty set using either several add calls, or a single call to update.
# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(3)
# print(empty_set)
# empty_set.clear()
# print(empty_set)
# # or we could use a loop to grab items from a range object:
# for number in range(1, 4):
# 	empty_set.add(number)
# print(empty_set)
#
# numbers = {"four", "five", "six"}
# empty_set.update(numbers)
# print(empty_set)
# empty_set.clear()
#
# # Exercice 3 Create a second set which includes at least one common element with the first set.
# numbers = {"seven", "eight", "seven"}
# empty_set.update(numbers)
# print(empty_set)
#
# # Exercice 4 Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
#
# print(set1.union(set2))
# print(set1.difference(set2))  # you can see that in this line and the next one the order matter as the result is different
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))

# # Exercice 5 Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or
# # not their number was within the range you specified.
# # If you want an extra challenge, also tell the user if their number was too high or too low.
# numbers = range(1, 11)
# number = int(input('Entrez un nombre compris entre 1 et 10 : '))
# if number in numbers:
# 	print(f"Bravo votre nombre est dans le range {numbers}")
# elif number > max(numbers):
# 	print("Votre nombre est au dessus du range")
# else:
# 	print("Votre nombre est au dessous du range")


###################
# Day12 Functions #
###################
# # Exercice 1 Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and
# # they should print the result of the arithmetic operation indicated by the function name.
# # When orders matters for an operation, the first argument should be treated as the left operand, and the second
# # argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result
# # should be 4, not -4.
# # You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you
# # should print a warning instead of calculating their division.
# def add(terme1, terme2):
#     print(f"{terme1 + terme2}")
#
#
# def substract(terme1, terme2):
#     print(f"{terme1 - terme2}")
#
#
# def divide(terme1, terme2):
#     print(f"{terme1 / terme2}")
#
#
# def multiply(terme1, terme2):
#     print(f"{terme1 * terme2}")
#
#
# add(5, 7)
# substract(terme1=10, terme2=5)
# divide(terme1=20, terme2=4)
# multiply(5, 4)

# # Exercice2 Define a function called print_show_info that has a single parameter. The argument passed to it will be a
# # dictionary with some information about a T.V. show. For example:
# #
# tv_show = {
#     "title": "Breaking Bad",
#     "seasons": 5,
#     "initial_release": 2008
# }
#
#
# #  print_show_info(tv_show)
# # The print_show_info function should print the information stored in the dictionary, in a nice way. For example:
# #  Breaking Bad (2008) - 5 seasons
# # Remember you must define your function before calling it!
#
#
# def print_show_tv(tv_show):
#     print(f"{tv_show.get('title', 'unknown')} ({tv_show.get('initial_release', 'unknow')}) - "
#           f"{tv_show.get('seasons', 'unknown')} seasons")
#
#
# #
# #
# # print_show_tv(tv_show)
# #
# # # Exercice 3 Below you’ll find a list containing details about multiple TV series.
# # #
# series = [
#     {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
#     {"title": "Fargo", "seasons": 4, "initial_release": 2014},
#     {"title": "Firefly", "seasons": 1, "initial_release": 2002},
#     {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
#     {"title": "True Detective", "seasons": 3, "initial_release": 2014},
#     {"title": "Westworld", "seasons": 3, "initial_release": 2016},
# ]
# # # Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for
# # # each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.
# for line in series:
#     print_show_tv(line)
#
# # Exercice 4 Create a function to test if a word is a palindrome. A palindrome is a string of characters that are
# # identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.
# word = "was it a car or a cat I saw"
#
#
# def is_apalindrome(word):
#     if word[::-1].lower().replace(" ", "") == word.lower().replace(" ", ""):
#         print("Il s'agit bien d'un palindrome")
#     else:
#         print("Desole ceci n'est pas un palindrome")
#
#
# is_apalindrome(word)
#
# # Project Reading list
# # The brief
# #
# # For this project the application needs to have the following functionality:
# #
# #     Users should be able to add a book to their reading list by providing a book title, an author's name, and a year
# #     of publication.
# #     The program should store information about all of these books in a Python list.
# #     Users should be able to display all the books in their reading list, and these books should be printed out in a
# #     user-friendly format.
# #     Users should be able to select these options from a text menu, and they should be able to perform multiple
# #     operations without restarting the program. You can see an example of a working menu in the post on while loops
# #     (day 8).
# #
# # This project is a bit larger than the ones we've tackled before, so make sure you tackle it one piece at a time.
# #
# # Something to note with this project is that because the books in the reading list are stored in a Python list, when
# # the program ends, the reading list data will be lost.
#

# menu_prompt = """Please select an option:  a to add, l to list the books"
# 'a' to add a book
# 'd' to delete a book
# 'l' to list a book
# 'r' to mak a book as read
# 's' to search for a book
# 'q' to quit
#
# What would you like to do ? """
#
# book_read = {}
# list_book_read = []
#
#
# def add():
#     title, author, year_of_pulbication = input(
#         f"Please provide the book title, author's name and year of publication "
#         f"separated by ,: ").split(',')
#     book_read = {"title": title.strip(), "author": author.strip(), "year": year_of_pulbication.strip(), "read": False}
#     list_book_read.append(book_read)
#
#
# def delete():
#     choix = input('Desirez vous effacer un titre(1), un auteur(2), une date(3) or q to quit : ')
#     if choix == 'q':
#         choix = 113
#     else:
#         choix = int(choix)
#
#     while choix != 113:
#         if choix == 1:
#             title = input("Saisissez le titre du livre a effacer : ")
#             i = 0
#             for book in list_book_read:
#                 if book.get("title") == title:
#                     del list_book_read[i]
#                 i += 1
#
#         if choix == 2:
#             for book in list_book_read:
#                 del book["author"]
#
#         if choix == 3:
#             for book in list_book_read:
#                 del book["year"]
#
#         choix = input('Desirez vous effacer un titre(1), un auteur(2), une date(3) or q to quit : ')
#         if choix == 'q':
#             choix = 113
#         else:
#             choix = int(choix)
#
#
# def list_books():
#     for book in list_book_read:
#         if book.get("read"):
#             print(book.get("title"), book.get("author"), book.get("year"))
#
#
# def mark():
#     title = input("Type the book title you've just red : ")
#     for book in list_book_read:
#         if book.get("title") == title:
#             book['read'] = True
#
#
# def search():
#     search_word = input('Please type a title or an author or a year of publication : ').strip()
#
#     for book in list_book_read:
#         if book.get("title") == search_word or book.get("author") == search_word or str(book.get("year").strip()) == str(search_word):
#             print(book.get("title"), book.get("author"), book.get("year"), book.get("read"))
#
#
# def quit():
#     exit(0)
#
#
# # Get a selection from the user
# selection_option = input(menu_prompt).strip().lower()
#
# while selection_option != 'q':
#     if selection_option == 'a':
#         add()
#     elif selection_option == 'd':
#         delete()
#     elif selection_option == 'l':
#         list_books()
#     elif selection_option == 'r':
#         mark()
#     elif selection_option == 's':
#         search()
#     else:
#         print(f"Sorry, {selection_option} isn't a valid option.")
#         break
#
#     selection_option = input(menu_prompt).strip().lower()

#########
# Day13 #
#########
# # Exercice 1 Define a exponentiate function that takes in two numbers. The first is the base, and the second is the
# # power to raise the base to. The function should return the result of this operation. Remember we can perform
# # exponentiation using the ** operator.
# def power(base, pw):
#     return base ** pw
#
#
# print(power(2, 2))
#
#
# # Exercice 2 Define a process_string function which takes in a string and returns a new string which has been converted
# # to lowercase, and has had any excess whitespace removed.
# def process_string(string):
#     return string.strip().lower()
#
#
# print(process_string(" HelLo "))

# # Exercice 3 Write a function that takes in a tuple containing information about an actor and returns this data as a
# # dictionary. The data should be in the following format:
# # ("Tom Hardy", "English", 42)  # name, nationality, age
# # You can choose whatever key names you like for the dictionary.
# actor, nationality, old = "Tom Hardy", "English", 42
# result = {"nom": {actor}, "nationalite": {nationality}, "age": {old}}
# for keys,values in result.items():
#     print(keys, values)

# # Exercice 4
# # Write a function that takes in a single number and returns True or False depending on whether or not the number is
# # prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.
#
# # Rappel sur comment trouver un nombre premier
# # Un nombre premier est un nombre divisible uniquement par 1 et lui meme.
# # 1/ Soit n le nombre dont nous voulons savoir si il est premier
# # 2/ on va chercher entre 2 et sqrt(n) au dela cela ne sert ex: prenons 35 sqrt(35) = 7 si on va au dela de 7 nous
# # reecrivons la meme chose mais dans l'autre sens ex: 5*7 <-> 7*5
# # 3/ Les criteres de divisibilite:
# #   - par 2, si son chiffre des unites est pair,
# #   - par 5, si son chiffre des unites est 0 ou 5,
# #   - par 10, si son chiffre des unites est 0,
# #   - par 3, si la somme de ses chiffres est divisible par 3,
# #   - par 9, si la somme de ses chiffres est divisible par 9.
#
# from math import sqrt, ceil
#
#
# def sum_divisible_par_trois(number):
#     array_nombre = []
#     for i in str(number):
#         array_nombre.append(int(i))
#     return sum(array_nombre) % 3
#
#
# def sum_divisible_par_neuf(number):
#     array_nombre = []
#     for i in str(number):
#         array_nombre.append(int(i))
#     return sum(array_nombre) % 9


# def prime(number):
#     if number == 0 or number == 1 or number == 2 or number == 3:
#         return True
#     else:
#         for i in range(2, ceil(sqrt(number))):
#             if number % 2 == 0:
#                 return False
#             elif number % 5 == 0 and number != 5:
#                 return False
#             elif number % 10 == 0:
#                 return False
#             elif sum_divisible_par_trois(number) % 3 == 0 and sum_divisible_par_trois(number) != 3:
#                 return False
#             elif sum_divisible_par_neuf(number) % 3 == 0 and sum_divisible_par_neuf(number) != 9:
#                 return False
#             else:
#                 return True
#
#
# if prime(83):
#     print("C'est un nombre premier")
# else:
#     print("Ce n'est pas un nombre premier")

# # Correction
# def is_prime(dividend):
#     if dividend < 2:
#         return False
#
#     for divisor in range(2, dividend):
#         if dividend % divisor == 0:
#             return False
#
#     return True
#
# print(is_prime(97))

#########
# Day14 #
#########
# # Exercice 1 Rewrite the following piece of code using a context manager:
# #
# #  f = open("hello_world.txt", "w")
# #  f.write("Hello, World!")
# #  f.close()
# #
# # Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
# with open("hello_world.txt", "w") as f:
#     f.write("Hello World! \n")
#
# # Exercice 2 Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
# with open("hello_world.txt", "a") as f:
#     f.write("How are you? \n")
#
# # Exercice 3 Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.
# # standard way to proceed:
# with open("iris.csv", "r") as iris_file:
#     iris_data = iris_file.readlines()
#
# headers = iris_data[0].strip().split("\t")
# irises = []
# for row in iris_data[1:]:
#     iris = row.strip().split("\t")
#     iris_dict = dict(zip(headers, iris))
#     irises.append(iris_dict)
#
# for line in irises:
#     print(line)
#
# # Using csv module
# import csv
#
# movies = [
#     {"name": "The Matrix", "director": "Wachowski"},
#     {"name": "Green Book", "director": "Farelly"},
#     {"name": "Amadeus", "director": "Forman"},
# ]
#
#
# def write_to_file(output):
#     with open("file.csv", "w") as f:
#         writer = csv.DictWriter(f, fieldnames=["name", "director"])
#         writer.writeheader()
#         writer.writerows(output)
#
#
# def read_from_file():
#     with open("file.csv", "r") as f:
#         reader = csv.DictReader(f)
#         for line in reader:
#             print(f"Name: {line['name']}\tDirector: {line['director']}")
#
#
# write_to_file(movies)
# read_from_file()

# # Project: Reading List
# # The brief
# #
# # For this project the application needs to have the following functionality:
# #
# #     Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# #     The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# #     Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# #     Users should be able to search for a specific book by providing a book title.
# #     Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).
# #
# # This project is much larger than the ones we've tackled before, so make sure you tackle it one piece at a time.
# #
# # If you want to challenge yourself, we also have a slightly harder version of the project that you can try, that has additional functionality.
# #
# import csv
#
#
# def write_to_file(output):
#     with open("file.csv", "w") as f:
#         writer = csv.DictWriter(f, fieldnames=["title", "author", "year", "read"])
#         writer.writeheader()
#         writer.writerows(output)
#
#
# def read_file(output):
#     with open("file.csv", "r") as f:
#         reader = csv.DictReader(f)
#         for line in reader:
#             print(f"Name: {line['title']}\tauthor: {line['author']}\tyear: {line['year']}\tread: {line['read']}")
#
#
# menu_prompt = """Please select an option:  a to add, l to list the books"
# 'a' to add a book
# 'd' to delete a book
# 'l' to list a book
# 'r' to mak a book as read
# 's' to search for a book
# 'q' to quit
#
# What would you like to do ? """
#
# book_read = {}
# list_book_read = []
#
#
# def add():
#     title, author, year_of_pulbication = input(
#         f"Please provide the book title, author's name and year of publication "
#         f"separated by ,: ").split(',')
#     book_read = {"title": title.strip(), "author": author.strip(), "year": year_of_pulbication.strip(), "read": False}
#     list_book_read.append(book_read)
#     write_to_file(list_book_read)
#
#
# def delete():
#     choix = input('Desirez vous effacer un titre(1), un auteur(2), une date(3) or q to quit : ')
#     if choix == 'q':
#         choix = 113
#     else:
#         choix = int(choix)
#
#     while choix != 113:
#         if choix == 1:
#             title = input("Saisissez le titre du livre a effacer : ")
#             i = 0
#             for book in list_book_read:
#                 if book.get("title") == title:
#                     del list_book_read[i]
#                 i += 1
#
#         if choix == 2:
#             for book in list_book_read:
#                 del book["author"]
#
#         if choix == 3:
#             for book in list_book_read:
#                 del book["year"]
#
#         choix = input('Desirez vous effacer un titre(1), un auteur(2), une date(3) or q to quit : ')
#         if choix == 'q':
#             choix = 113
#         else:
#             choix = int(choix)
#
#
# def list_books():
#     read_file(list_book_read)
#
#
# def mark():
#     title = input("Type the book title you've just red : ")
#     for book in list_book_read:
#         if book.get("title") == title:
#             book['read'] = True
#     write_to_file(list_book_read)
#
#
# def search():
#     search_word = input('Please type a title or an author or a year of publication : ').strip()
#
#     for book in list_book_read:
#         if book.get("title") == search_word or book.get("author") == search_word or str(
#                 book.get("year").strip()) == str(search_word):
#             print(book.get("title"), book.get("author"), book.get("year"), book.get("read"))
#
#
# def quit():
#     exit(0)
#
#
# # Get a selection from the user
# selection_option = input(menu_prompt).strip().lower()
#
# while selection_option != 'q':
#     if selection_option == 'a':
#         add()
#     elif selection_option == 'd':
#         delete()
#     elif selection_option == 'l':
#         list_books()
#     elif selection_option == 'r':
#         mark()
#     elif selection_option == 's':
#         search()
#     else:
#         print(f"Sorry, {selection_option} isn't a valid option.")
#         break
#
#     selection_option = input(menu_prompt).strip().lower()

#########
# Day15 #
#########
# # Exercice 1 Convert the following for loop into a comprehension:
#
# numbers = [1, 2, 3, 4, 5]
# #squares = []
# #
# # for number in numbers:
# # 	squares.append(number ** 2)
#
# squares = [number**2 for number in numbers]
# print(squares)

# # Exercice 2 Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the
# # values is title case.
# #
# movie = {
# 	"title": "thor: ragnarok",
# 	"director": "taika waititi",
# 	"producer": "kevin feige",
# 	"production_company": "marvel studios"
# }
# #
# # Remember that iterating over a dictionary only gives us the keys by default. You can use the items method to get the
# # keys and the values. See day 10 for more details.
# result = {key: value for key, value in movie.items()}
# print(result)



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

# # Exercice 4 Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an
# # argument for print function's sep parameter for this exercise.
# print(*range(1, 21), sep=", ")
#
# # Exercice 5 Modify your code from exercise 4 so that each number prints on a different line. You can only use a single
# # print call.
# print(*range(1, 21), sep="\n")

# ----------------------------------

# #########
# # Day18 #
# #########
# # Exercice 1 Import the fractions module and create a Fraction from the float 2.25. You can find information on how to
# # create fractions in the documentation.
# from fractions import Fraction
#
# print(Fraction(2.25))
#
# # Exercice 2 Import only the fsum function from the math module and use it to find the sum of the following series of
# # floats:
# from math import fsum
#
# numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
# print(fsum(numbers))
#
# # Exercice 3 Import the random module using an alias, and find a random number between 1 and 100 using the randint
# # function. You can find documentation for this function here.
# import random as rd
#
# x = rd.randint(1, 100)
# print(x)

# # Exercice 4 Use the randint function from the exercise above to create a new version of the guessing game we made in
# # day 8. This time the program should generate a random number, and you should tell the user whether their guess was
# # too high, or too low, until they get the right number.
# import random
# x = random.randint(1, 10)
# reponse = int(input("Devinez un nombre tirez au hasard entre 1 et 10 : "))
# print(x)
# while reponse != x:
#     if reponse < x:
#         print("your number is too low")
#     elif reponse > x:
#         print("your number is too high")
#     reponse = int(input("Essayez encore, devinez un nombre tirez au hasard entre 1 et 10 : "))

# Project: JSON Reading List
