"""
Name:   problem1.py

Purpose: This problem requires a celsius to fahrenheit converter to help the user understand the amount of degrees celsius to fahrenheit

Author: Au.E

Date: 07/12/2020
"""

c = float(input("Degrees celsius: "))

#Tells user the amount of degrees fahrenheit after conversion
print(c , "degrees celsius equals", float((9/5) * (c) + (32) ), "degrees fahrenheit.")
