name1=["ales","Mark","Deny","Hendry"]
name2=name1
name3=name1[:]

name1=["Anand"]
name3=["Murugan"]

sum=0

for ls in (name1,name2,name3):
	if ls[0]=="Anand":
		sum+=1
		pass
	if ls[1]=="Murugan":
		sum+=5
	print(sum)
	pass