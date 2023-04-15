
import math

height = int(input("what is your height in cm: "))
weight = int(input("What is your weigth in kg: "))
bmi = math.ceil(weight/((height/100)**2))

print("Your BMI is" + bmi)

if bmi >= 35:
    print("OYou are severly Obese")
elif bmi >= 34.9:
    print("You are Obese")
elif bmi >= 29.9:
    print("You are Overweight")
elif bmi >= 24.9:
    print("You are Normal")
elif bmi >=18.5:
    print("You are Underweight")
else:
    print("You are severly Underweight")
