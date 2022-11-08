# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index_bmi = round(weight / (height ** 2), 1)
if index_bmi < 18.5:
    print(f"Your BMI is {index_bmi}, you are underweight.")
if index_bmi >= 18.5:
    if index_bmi < 25:
        print(f"Your BMI is {index_bmi}, you have a normal weight.")
if index_bmi >= 25:
    print(f"{index_bmi}")
    if index_bmi < 30:
        print(f"Your BMI is {index_bmi}, you are slightly overweight.")
if index_bmi >= 30:
    if index_bmi < 35:
        print(f"Your BMI is {index_bmi}, you are obese.")
    else:
        print(f"Your BMI is {index_bmi}, you are clinically obese.")

