#import Array package 
import array
n = int(input("Enter the Size of array "))
arr =[]
for x in range(n):
	x = int(input("Element array "))
	arr.append(x) # X value asign to Array
	pass

#Sorted Array 
sortedArray = sorted(array.array(('i'),arr))
for i in range(len(arr)-1,0,-1):
	if sortedArray[i]!=sortedArray[i-1]:
		print(f"sorted number array {sortedArray[i-1]}")
		break
		pass
	pass