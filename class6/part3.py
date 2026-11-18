# x=int(input())
# if x%3==0 and x%5 == 0:
#     #dont type "if (x%3 and x%5) == 0:"
#  print("Fizz Buzz")
# if (x%3 ==0 and x%5!= 0):
#    print("Fizz")
# if (x%5 == 0 and x%3!= 0):
#     print("Buzz")


# x= int(input())
# if x%2==0:
#   x=x+5
# else:
#   x=x+11
# print(x)

# x=int(input())
# if x>20:
#     x=x+25
# elif x>10:
#     x=x+15
# print(x)


# x=int(input())
# if x>=18:
#  print("can vote")
# else:
#     print("can't vote")

# Write your reference solution here
p1=input().strip().lower()
p2=input().strip().lower()

if p1=="rock" and (p2=="paper" or p2=="scissors"):
    print("Player 1 wins")
elif p2=="rock" and (p1=="paper" or p1=="scissors"):
    print("Player 2 wins")
elif p1=="paper" and p2=="scissors":
    print("Player 2 wins")
elif p2=="paper" and p1=="scissors":
    print("Player 1 wins")
else:
    print("Draw")