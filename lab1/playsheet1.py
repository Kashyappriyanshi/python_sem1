print("Your name is:", input("Enter your name: "))
print("==== WELCOME ====\nName:\tPriyanshi\nHobby:\tPainting\n==================")
# /n for new line, /t for tab space
name = input("Enter your name: ")
print(name)
#with split, this entire code can be used for making list
values = input("Enter three flowers: ").split()
print(values)
#without split, this will not make a list
values = input("Enter three fruits: ")
print(values)
#
numbers = list(map(int, input("Enter three numbers:").split()))
print(numbers)