guest = ['pinkmen','eric','hawkins']
message = "welcome to the dinner party"
print("hi"+" " + guest[0] +" "+ message)
print("hi"+" " + guest[1] +" " + message)
print("hi"+" " + guest[2] +" "  + message)
# Add a print statement at the
#end of your program stating the name of the guest who can’t make it.
print(guest[0] +"  " + "will not be able to make it:(")

#Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting
guest.remove('pinkmen')
guest.insert(0,'john')
#Print a second set of invitation messages, one for each person who is still
#in your list.
print("\nhi"+" " + guest[0] +" " + message)
print("hi"+" " + guest[1] +" " + message)
print("hi"+" " + guest[2] +" " + message)
#. Add a print
#statement to the end of your program informing people that you found a
#bigger dinner table.
print("guyz i just found a bigger dining table i think i should invie some moere peoples")

print("\n"+"\n")
guest.insert(0,'poplamon')
guest.insert(0,'beepkiboo')
guest.append('rahul')
print(guest)
print("hi"+" " + guest[0] +" "+ message)
print("hi"+" " + guest[1] +" " + message)
print("hi"+" " + guest[2] +" "  + message)
print("hi"+" " + guest[3] +" "+ message)
print("hi"+" " + guest[4] +" " + message)
print("hi"+" " + guest[5] +" " + message)

# You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
print("unfortunatly new table didnt arrive on time now i can invite only two peooples")

print("\n"+"\n")
p1 = guest.pop()
p2 = guest.pop()
p3 = guest.pop()
p4 = guest.pop()
print("hi"+" "+p1+" "+"sorry i cant invite u")
print("hi"+" "+p2+" "+"sorry i cant invite u")
print("hi"+" "+p3+" "+"sorry i cant invite u")
print("hi"+" "+p4+" "+"sorry i cant invite u")

print(guest)
print("\n")
print("hi"+" " + guest[0] +" "+ message)
print("hi"+" " + guest[1] +" " + message)
