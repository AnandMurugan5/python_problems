n=int(input("Enter Number "))
print("Before the Number" %n)
rev=0
while n!=0:
	rev = rev*10 + n%10
	n=(n/10)
	print("after " %rev)
	pass