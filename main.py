import matplotlib.pyplot as plt
import numpy as np
import string
from meter import draw_meter # this imports code from another file in our folder
'''
password_strength.py: A module to check the strength of a password provided
by a user.
This should not be used for actual passwords; instead it is simply a coding
exercise.
Jake Hart
CIS 162 - SECTION YOUR SECTION
10/09/26 
'''
score = int(0) #This sets a score variable to 0 so that later score can determine the color on the graph.
print("My Password Strength Checker")
print("       By Jake Hart")
print("")
password = input("Enter your password: ") #asks the user for thier password
digits = any(char.isdigit() for char in password) # this looks to see if their are any numbers in the passwords and if their are it sets the variable to True
special = any(char in string.punctuation for char in password) # this does what the line above it does but with special characters
password_length = int(len(password)) # this sees how long the passoword is
color = "red" # this is here so that color can be set to something that is later changed
if password != password.lower(): #this checks to make sure that all the characters in my password are NOT loercase
       score += 10 #everytime you see this it maeans we are adding or subtracting to the score
if password != password.upper(): #THis checks to make sure that all the characters in the password are NOT upercase
       score += 10
if special == True: # This is just here to add points to the score if their are special characters in the password
       score += 10
if digits == True: # This is just here to add points to the score if their are numbers in the password
       score += 10
if password_length >= 12: # This line and the 3 lines below it are here to give a certain amount of points depending on how long the password is
       score += 10
elif password_length > 8 and password_length < 12:
       score +=5
if "apple" in password: #This line and the 9 lines below it are here so that the score loses a point if the passowrd has one of these common words in it
       score -= 1
if "girl" in password:
       score -= 1
if "password" in password:
       score -= 1
if "love" in password:
       score -= 1
if "dog" in password:
       score -= 1
if score > 40: #if the score is grater than 40, it will change the collore
       color = "yellow" # changing the color is import so that the line on the meter we print points to a different color
if score > 45:
       color = "green"


draw_meter(score, color) #this is waht we imported from the other file. It creates a graph that depending on the score 

#1. #What resources did you use to help you complete this project?
       # I used what we learned in class, all code supplied to me, what i learned in my previous coding classes from python, and google ai to find out why certain errors were happening like a syntax error for example.
#2. How many hours did you spend (roughly) on the project?
       # I would say I put around 8 hours into this project.
#3. How many times did you attend office hours, the Success Center, or Python Wave?
       # 0 Times, but I did ask you questions in class about it.
#4. What part of the project was the toughest?
       # I was having the most dificulty makin the image print correctly. The color kept printing red when it wasnt supposed to.
#5. Did you experience any issues using the Github Codespace for coding? If so, please note the issues you experienced.
       # Well up untill late last week I wasnt correctly saving my code. My meter also was creating incorect graphs.
#6. Why do you think we ask you to provide comments in the code?
       # To make sure that it is us doing the work and to also make sure we know what everything we type does.
#7. What was your prior programming experience before this course (it is perfectly fine to say 'None').
       # I had 3 coding classes in highschool (Block coding, intro to python, and java) and a cybersecurity class.
#8. Lookup the documentation for Python's len() function here. What can it be used on besides strings? What will it return if a length is too large?
       # len() can also be used for other sequences like bytes, tuples, lists, and ranges.
#9. Research other techniques that are used to create a strong password. What are three mistakes people often make when creating a password?
       # You can combine 3 or 4 random words together to make a password that is eassy to remember but hard to guess. People who use the same password for every website get screwed if a data breach happens. If you use personal information in your passoword it makes it easier to guess. Using common words/sequences used in a password like "123" or "password" can make your password esay to guess. 
#10. Currently, if the user enters an empty password the program still evaluates its score (though it will evaluate to 0). What might be a better way of handling the situation when a user enters an empty password?
       # I think it would be best to make it so that if the user enters nothing as the password it would jsut ask the user to enter the password again, forcing them to give an input.