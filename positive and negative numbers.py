#negative and positive numbers
n=int(input("enter the no of elements in list:"))
x=list(map(int,input().split()))
ng=[]
ps=[]
for  i in range(n):
    
    if x[i]<0:
        ng.append(x[i])
    else:
        ps.append(x[i])
ng.extend(ps)
print(ng)
