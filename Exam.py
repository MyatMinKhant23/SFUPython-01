x = int(input("Enter Your Number: "))
	
if x < 101 and x > 89 or x == 100:
	print("A")
elif x <= 89 and x > 79:
	print("B")
elif x <= 79 and x > 59:
	print("c")
elif x <= 59 and x > 49:
	print("D")
elif x <= 49 and x > 0 or x == 0:
	print("F")
else:
	print("Check again")

