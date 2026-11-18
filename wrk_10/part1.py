#q: sum of each column and row all separatly 
n=input().split()
R=int(n[0])
C=int(n[1])

i=0
s=[[1,2,3],[4,5,6],[7,8,9]]
while i<R:
    j=0
    total=0
    while j<C:
        t=int(s[i][j])
        total=total+t
        j=j+1
    print(total,end=" ")
    i=i+1

# done till b5, try b3.


