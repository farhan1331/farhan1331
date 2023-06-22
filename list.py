#example of lists
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print(bicycle[0])
print(bicycle[1].upper())
print(bicycle[-1].title())
message = "my first bycicle was a"+" "+bicycle[0]+"."
print(message)
#try it your self
#3-1. Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
#person’s name.

names = ['walter','pinkmen','jerry']
print(names[0:3])
message1 = "thanks for coming today"
print("hi"+" "+names[0]+" "+message1)
print("hi"+" "+names[1]+" "+message1)
print("hi"+" "+names[2]+" "+message1)
#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
veicle = ['bugati','honda','lamborgini','pourse']
statement ="i would liken to drive"
print(statement+" "+veicle[0])
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = "dugati"
print(motorcycles)
motorcycles.append('dugati')
print(motorcycles)


#2 apend , insert ,del, remove and pop
motorcycles1 =[]
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)
motorcycles1.insert(0,'dugati')
print(motorcycles1)
del motorcycles1[0]
print(motorcycles1)
popped_motorcycles1 = motorcycles1.pop()
print(motorcycles1)
print(popped_motorcycles1)
motorcycles1.remove('honda')
print(motorcycles1)
