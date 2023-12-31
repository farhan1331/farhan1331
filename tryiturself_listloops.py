#Use a for loop to print the numbers from 1 to 20,
#inclusive.
for loop in range(1,21):
	print(loop)
#done
print()
print()
print()

#Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers. (If the output is taking too long, stop it by
#pressing ctrl-C or by closing the output window.)

#millions = [list(range(1,10000000))]
#for loop1 in millions:
#	print(loop1)

#done

print()
print()
print()

#Odd Numbers: Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number.
for odd in range(1,21,2):
    print(odd)
#done
print()
print()

#Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#done
print()
print()
print()

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

for i in range(0,31,3):
   print(i)

#done

print()
print()
print()
#Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

cube = [value**3 for value in range(1,11)]      
print(cube)
