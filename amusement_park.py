#•	 Admission for anyone under age 4 is free.
#•	 Admission for anyone between the ages of 4 and 18 is $5.
#•	 Admission for anyone age 18 or older is $10.
age = 12
if  (age >=1 and age<4):
	price = 0
elif(age >=4 and age<18):
    price = 5
elif age > 65:
	price = 5
else :
	price = 10

	
print("Your admission cost is $" + str(price) + ".")

	
