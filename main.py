import matplotlib.pyplot as plt
import numpy as np
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
password = input(" Enter your password: ")




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