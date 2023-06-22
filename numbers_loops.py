
#using range function

for value in range(1,5):
    print(value)
 
 #using range to make a list
numbers = list(range(1,5))
print(numbers)
 #skiping numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares
squares = []
for value in range(1,11):
     square = value**2
     squares.append(square)
     print(squares)
#--------------------------------"
#my method                       |
#squares = []                    |
#for value in range(1,11):       |
#     squares = value**2         |   
#     print(squares)             |
#--------------------------------"

print()
print()
print()


#min max sum
digits = [1,2,3,4,5,6,7,8,9,0]
min (digits)
max(digits)
sum(digits)

#better method
squares = [value**2 for value in range(1,11)]
print(squares)


print()
print()
print()

#slicing the list 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#print(players[:4])
#print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
        print(player.title())


print()
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[2:]
my_foods.append('cnaoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
