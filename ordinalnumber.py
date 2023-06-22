#•	 Store the numbers 1 through 9 in a list.

numbers = [1,2,3,4,5,6,7,8,9]
for value in numbers:
	print (value)
	
print()

for value in numbers:
    if value < 3:
        print ("\n"+str(value)+"st")
    elif value == 3:
        print("\n"+str(value)+"rd")
    else:
        print("\n"+str(value)+'th')
