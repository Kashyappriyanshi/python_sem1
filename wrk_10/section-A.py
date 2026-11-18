# A1-
# Given:
# input: 4 then 7 7 2 9(one per line)
# n = int(input())
# arr = []
# i = 0
# while i < n:
#     arr.append(int(input()))
#     i += 1
# print(len(arr), arr[0], arr[n-1])
# n=int(input())
# R=len()
# d = 0
# while d <= R + C - 2:
#     i = 0

#     while i < R:
#         j = d - i

#         if 0 <= j < C:
#             print(m[i][j], end=" ")

#         i += 1

#     d += 1

#transpose in matrix:
# s=input().split()
# R=int(s[0])
# C=int(s[1])

# m=[]
# j=0
# n=input().split()
# while j<C:
#     i=0
#     row=[]
#     while i<R:
#         row.append(int(n[i][j]))
#         i+=1
#     m.append(row)
#     j+=1

# i=0
# while i<len(t):
#     j=0
#     row=[]
#     while j<


m = [[1,2,3],[4,5,6],[7,8,9]]
i =0
t = []
R = len(m)
C = len(m[0])
while i< R:
    j = i
    while j<C:
        m[i][j],m[j][i]=m[j][i],m[i][j]
        j+=1
    i+=1
i = 0
while i<R:
    j = 0
    while j <C:
        print(m[i][j],end=" ")
        j+=1
    print()
    i+=1
