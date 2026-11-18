# for i in range(5,10):#5 included 10 NOT
#     print(i)

# for i in range(5,10,2):# jumpsto every 2nd number
#     print(i)

#continue -"skips" everything afterwrds and continue with the loop(ofc iteration happens)

# #D1-
# n=int(input())
# for i in range(1,11):
#     print(n*i)

#D2-
# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# #here i and j is NOT INDEX, it's THE VALUE ITSELF
# #isse pehle hm index pe iterate kr rhe the but yaha hm list pe hi seedha iterate kr rhe hai
# for i in mat:
#     sum=0
#     for j in i:
#         sum+=j
#     print(sum,end=" ")

#E1-
n=int(input())
#create a dictionary
for i in range(n):
    l=input().split()
    name=l[0]
    marks=int(l[1])
    marks_lecun[name]=marks#key-value pair
print(marks_lecun)

#iterate over a dictionary
sum=0
max marks=-99 #or 0 would work too.
for mark in marks_lecun.value():
    sum+=mark
    if mark>max_marks:
        max_marks=max(mark,max_marks)
    print(max_marks)
