n = int(input("Enter the Number\n "))
a=[]
for i in  range(0,n):
 elemt=int(input("Enter the Elemt number"))
a.append(elemt)
avg=sum(a)/n
print("The AVg value is ",round(avg,2))