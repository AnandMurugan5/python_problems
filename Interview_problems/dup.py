import array
arr=[]
count=[]
n= int(input("Enter size of array "))
for x in range(n):
    count.append(0)
    x=int(input("Enter The arry: "))
    arr.append(x)
print("Array elemet remov duplicate")
for x in range(n):
    count[arr[x]]=count[arr[x]]+1
    if count[arr[x]]==1:
        print(arr[x])
