weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cm: "))

bmi = weight / (height * height)
height=height/100

if bmi < 18.5:
    category = "Under weight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"Your bmi is: {bmi}")
print(f"Your category is: {category}")

