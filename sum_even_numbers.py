numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#iitialize the sum variables
sum_of_even=0
#iterte over each number in a list
for number in numbers:
    if number % 2 == 0:
        sum_of_even += number
print(f"Sum of even numbers: {sum_of_even}")


numbers=[1,2,1,2,8,5,7,4,7,8,4,5,8,5,8,2,5]
sum_of_odd=0
for number in numbers:
	if number % 2 != 0:
		sum_of_odd += number
print(f"The sum of odd numbers: {sum_of_odd}")

x=[1,2,8,5,8,5,8,5,8,2,5,2]
product_of_even=1
for i in x:
	if i % 2 == 0:
		product_of_even *= i
print(f"The product of the even numbers: {product_of_even}")

x=[25,25,25,26,24,28,27,29]
product_of_odd=1
for i in x:
	if i % 2 != 0:
		product_of_odd *= i
print(f"The product of odd numbers: {product_of_odd}")


n=[8,5,8,6,9,74,12,25,42,15,25]
product_of_odd=1
for i in n:
	if i % 2 !=0:
		product_of_odd *=i
print(f"The product of odd numbers: {product_of_odd}")


x=[1,2,5,2,5,4,7,8,9,56,8]
product_of_even=1
for i in x:
	if i % 2 == 0:
		product_of_even *=i
print(f"The sum of even numbers: {product_of_even}")



d=[9,98,7,6,5,4,3]
sum_of_odd=0
for i in d:
	sum_of_odd +=i
print(f"THe sum of odd numbers: {sum_of_odd}")



