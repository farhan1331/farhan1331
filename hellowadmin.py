#5-8. Hello Admin:
users = ['farhan','admin','eric','leo','diego']
name = 'udgh'
if name != 'admin' and name  in users:
	print("hi ",name,"how are u ")
elif name == 'admin' in users:
	print(" Hello admin, would you like to see a status report?")

elif len(users) == 0:
	print("there are no user we needs to find someone")

elif name not in users:
	print("your name is not on list would u like to creat an account")

else:
	print("something wents wrong")
