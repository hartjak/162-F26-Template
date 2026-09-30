import matplotlib.pyplot as plt
import numpy as np
import string
'''
password_strength.py: A module to check the strength of a password provided
by a user.
This should not be used for actual passwords; instead it is simply a coding
exercise.
Jake Hart
CIS 162 - SECTION YOUR SECTION
09/21/26 
'''
score = int(0)
print("My Password Strength Checker")
print("       By Jake Hart")
print("")
password = input("Enter your password: ")
digits = any(char.isdigit() for char in password)
special = any(char in string.punctuation for char in password)
password_length = int(len(password))
color = "red"
if password != password.lower():
       score += 10
if password != password.upper():
       score += 10
if special == True:
       score += 10
if digits == True:
       score += 10
if password_length >= 12:
       score += 10
elif password_length > 8 and password_length < 12:
       score +=5
if "apple" in password:
       score -= 1
if "girl" in password:
       score -= 1
if "password" in password:
       score -= 1
if "love" in password:
       score -= 1
if "dog" in password:
       score -= 1
if score < 45:
       color = "green"
elif score < 40:
       color = "yellow"

print(score)




# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()