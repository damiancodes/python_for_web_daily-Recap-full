num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+,-,8,/): ")

#perform the calculation based on operator

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero!"
else:
    result = "invalid operator"
print(f"Your result is: {result}")





num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

operator = input("Enter the operator (+,/-*):")

if operator == "+":
    result = num2 + num1
elif operator == "-":
    result = num2 - num1
elif operator == "/":
    result = num2 / num1

print(f"The results is: {result} ")


x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

operator = input("Enter the operator:(+,-,/,*)")
if operator == "+":
    result= x+y
elif operator == "*":
    result= x*y
else:
    result= x//y

print(f"The result is: {result}")