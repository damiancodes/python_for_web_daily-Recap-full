# to check if a number is odd or even
num10 = int(input("Enter a number: "))

if num10 % 2 == 0:
    print(f"{num10} is even")
else:
    print(f"{num10} is odd")



age = int(input("How old are you? "))

if age >= 18:
    print(f"You are {age} years old. You are an adult.")
else:
    print(f"You are {age} years old. You are a minor.")
