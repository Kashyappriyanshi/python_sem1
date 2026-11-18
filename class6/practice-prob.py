# # q25.
# n=int(input())
# if n>=18:
#  print("you can vote.")


# # q26.
# n=int(input())
# if n>1000:
#     s=n*0.1
#     print("Discounted price:Rs.", f"{s:.2f}")


# # q27.
# n=int(input())
# s=(n/150)*100
# if s>=90:
#     print(f"Merit scholarship awarded. Percentage: {s:.2f}%")
# # format string always give output in string. and it could be used the way it's been sued here.


# # q28.
# q1=int(input())
# q2=int(input())
# q3=int(input())
# avg=(q1+q2+q3)/3
# if 0>=q1>=100 and 0>=q2>=100 and 0>=q3>=100:
#   if avg>80 and (q1>=60 and q2>=60 and q3>=60):
#     print("Distinction Awarded")


# # q29.
# n=int(input())
# if n%2==0:
#     print("Even")
# else:
#     print("odd")


# # q30.
# n=int(input())
# s=n*1.50
# r=n*2.50
# if n<=100:
#     print("Bill:Rs.",s)
# else:
#     print("Bill:Rs.",r)

# # q31.
# n=int(input())
# if (n%4==0 and n%100!=0) or (n%400==0):
#     print("Leap Year")
# else: 
#     print("not a leap year")

# # q32.
# n=float(input())
# s=50
# r=50+15*(n-2)
# if n==0:
#     print("No trip.")
# elif n<=2:
#     print("Fare:",s)
# elif n>2:
#     print("Fare:",r)


# # q33
# n=(int(input()))
# if n>0:
#     print("Positive")
# if n%2==0:
#     print("Even")
# if n>100:
#     print("Large")
# if  not n>0 and not n%2==0 and not n>100:
#     print("None")

# n = 10
# while n <10:
#     if n<=2:
#         print("Even")
    # else:
    #     print("Odd")
    # n +=1 
    # print(n)   
# if n == 16:
#     print("Multiple of 4")
# else:
#     print("Not a multiple 4")  
# print("done")  

# n = 10
# if n %2 == 0:
#     print("e") 
# print("c") 
# else:
#     print("b")  
# n=int(input())
# i=1
# while i<=n:
#     if x>=y and x>=z:
#     x=int(input())
#     i+=1
#         print(x)
#     elif y>=x and y>=z:
#         print(y)
#     else:
#         print(z)

# i=0
# while i<5:
#     print(i)
#     # if i==3:
#     # break
#     i+=1
# else:
#     print("not <5")


# from token_source import TokenSource
# def main():
# src = TokenSource([4, 8, 15, 16, 23])
# i= 0
# n=0
# while i<len(src):
#     s=src[i]
#     if s>n:
#         n=s
#     i+1=i

# print(n)
# main()
 
# n=4827
# count=0
# while n>0:
#     count=count+1
#     n//=10

# print(count)


n = list(map(int,input().split()))
arr = []
i = 1
while i < n[0]:
    arr.append(n[i])
    i += 1
print(len(arr), arr[0], arr[-1])

