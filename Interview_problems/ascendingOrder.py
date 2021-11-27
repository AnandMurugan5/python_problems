n = int(input("ENter the numbers\n "))
h = list(map(int,input().split(' ')))
k,a = 0,0
p=[]
for i in range(0,n):
    v=h[i]
    if h[i] == max(h):
        k=0
    else:
        for j in range(v+1,max(h)+1):
            if j in h:
                if j > v:
                    k=j
                    break
    m=h[i]
    if h[i] == min(h):
        a = 0
    else:
        for s in range(0,h[i]):
            if s in h:
                if s < m:
                    a = s
    p.append(a+k)
    for i in range(0,n):
        print(p[i],end=' ')
