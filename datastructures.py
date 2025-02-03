# list datastructures
# uses the box bucket
# lists are mutable(changeable)
# lists are ordered
# lists have indexes

fruits=['apple','banana','mangoes','pineapple', 'orange' ,'pear']
print(fruits)
fruits[2]='watermelon'
fruits[4]='apple'
print(f"I love eating {fruits[2]}")
print(f"I love {fruits[4]}")

numbers=[1,2,3,4,5,6,7,8]
numbers.append(9)
# numbers.pop(9)
# numbers.count(9)
print (numbers[1:4])

#tuple datastructures
# tuples are imutable(you cant change them)
# tuples are ordered.

cars=('BMW', 'Audi', 'Subaru' ,'Mercedes' ,'Toyota' ,'Nissan')
print(cars[3])
nambari=(1,2,3,4,5,6,7,8,9)
print (len(nambari))

# set datastructures
days={'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
print(days)
#sets are unordered
#sets dont have indexes
#cant be changed imutable


clubs=['Arsenal', 'manchester', 'Gormahia' ,'AFC']
# print(clubs[2:])
clubs.append('Harambee')
print(clubs)

vegetables=('cabbages','onions', 'kales' ,'carrots')
print(vegetables)
print(len(vegetables))
print(vegetables[2])

my_set={1,2,3,4,5,6,7,8,9}
my_set.add(10)
print(my_set)


#dictionary data structures
#imutable
student={'Name': "John", 'Age': 18, "Gender": "Male" ,"school": "Emobilis"}
print(student)
print(student['Name'])
print(student['Age'])
