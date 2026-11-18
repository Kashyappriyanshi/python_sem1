# greet#this will give error,we know why
# def greet():
#     print("hello")

# greet#but since this is now an object, so it will not give error
#greet()#but this will call the function, this is NOT an object it is function

#x=greet #this will store address of the "greet" 
#x=greet()#this will store the value of return if it had any.
# print(greet)


# def greet(name):#name=parameter
#     print("hello")

# greet("shivatmika")#no arugument given when 1 should be given
# #"abc"= argument
# greet("shivatmika", "priyanshi")#2 aruguments given when atmost and atleast 1 could be taken.


# def add(a,b):
#     print (a+b)#this will answer back 30,ie, (a+b)
#     return 200

# x=add(10,20)#x will store the value of return
# print(x)


# def add(a,b):
#     print (a+b)#this will answer back 30,ie, (a+b)

# x=add(10,20)#this will answer back "none"
# print(x)
# x()

#-------"is" compares the memory location that any variable(if there's any) is pointing at.-------------



# def square(n):
#     return n*n

# def cube(n):
#     return n*n*n

# toolbox=[square, cube]
# print(toolbox[0](2))
# print(toolbox[1](2))


#----------------------lambda function----------------------------------
# ifEven=lambda a: True if a%2==0 else False
# print(ifEven(5))

# #---lambda with sorted
##key hamesha sorted me hi use hota hai
# words=["Banana", "apple", "fig"]
# # print(sorted(words,key=len))
# print(sorted(words,key=lambda w:len(w)))#upar vale function ka lamba version 

# print(sorted(words,key=str.lower))

# def last_char(words):
#     return words[-1]
# words=["apple", "Banana", "fig"]
# print(sorted(words,key=lambda w:w[-1]))#lambda me string ja rhi hai
# print(sorted(words,key=lambda w:True if w[::-1]==w else False))

# w=[1,2,3,4]
# def newObject(a):
#     w.append(a)
# print(w)
# newObject(5)
# print(w)


name="python"
name= name+" programming"
print(name)