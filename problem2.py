"""
Name:   problem2.py

Purpose: This problem is meant for determining how to fairly split the chicken that was won amongst the class and Mr. Fabroa.

Author: Au.E

Date: 07/12/2020
"""
#input data for amount of chicken
chicken = int(input("how many pieces of chicken are there?"))
students = int(input("how many students are there?"))
distributed_pieces = round(chicken/students)
Mr_fabroas_pieces = (chicken % students)
print ("each student gets:", distributed_pieces, "and Mr.Fabroa gets:", Mr_fabroas_pieces)
