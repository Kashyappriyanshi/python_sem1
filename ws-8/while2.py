# while True:
#     cmd=input("cmd> ")
#     if cmd=="quit":
#         print("bye")
#         break
#     print("you said:", cmd)   
attempts=0
while True:
    pin=input("pin:")
    attempts+=1
    if pin=="0000":
        print("unlocked")
        break
    if attempts==5:
        print("card blocked")
        break
    else:
        print("invalid pin,")
    print("invalid pin, try again", 5-attempts,"attempts left")
    