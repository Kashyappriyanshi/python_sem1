# names="python"
# scores=[95,87,90]
# scores[0]=98
# # print(len(scores))
# scores.append(99)
# print(scores)
# #lens work on list too bcs string is a list of characters
# #{} is set [] is list. list is an ordered data structure but set isn't.set is collection of unique elements.
# extra={95,87,90}
# print(extra)
# #append is adding at the end but for set a number can get added but not always at end rather randomly
# #index's concept is based on order and that doesn't exist in set so it is of no use in set.
# # s = "hello"
# # s[0] = "H"
# # print(s)
# #string is immutable. python doesn't changing the existing sting but create a new one. 
# #why does python do this? to *promote memory reuse*. thats why two names pointing to same value will give the same id.
# fruit="mango"
# fruit=fruit.upper
# print(fruit)
# #s.upper ekk naya string bnata hai so different id.
# l=[1,2,3,"h dh hbcdhb",0.8,]
# l=[1,2,3,[9,10],0.8]
# print(len(l))
# names = "Python"
# scores = [95, 87, 92]
# tags = {"Python", "AI", "Beginner"}
# print(names[1])
# print(scores[1])
# print(tags[1])
# #In Python, tags is a set (defined using curly braces {}). Sets are unordered collections of unique items. Because they do not keep items in any specific order, they do not have index numbers.
# print(type("hello"))
# print(type([1, 2, 3]))
# print(type({1, 2, 3}))
# print(type({}))
# print(type (set()))
# s = "hello"
# s[0] = "H"
# lst = [10, 20, 30]
# print(id(lst))
# lst[0] = 99
# print(id(lst))
# s = {1, 2, 3}
# s.add(42)
# s.add("hello")
# s.add((10, 20))
# s.add([1, 2])
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1][2])
# print(matrix[0][0])
# print(matrix[2][1])
# coords = {(0, 0), (1, 2), (3, 4), (1, 2)}

# print(coords)
# print(len(coords))
# article_tags = [
#     {"Python", "AI"},
#     {"Python", "Web"},
#     {"AI", "ML"},
# ]

# print(article_tags[0])
# print("AI" in article_tags[1])
# print(len(article_tags))
# data = [
#     ("Alice", {95, 87, 92}),
#     ("Bob", {78, 85, 90}),
# ]

# print(data[0][0])
# print(data[1][1])
# print(88 in data[0][1])
# l=(10,[20,30])
# print(id(l))
# l[0]=5
# print(id(l))
# print(hash(l))
# n= input()
# print("hello"+n )
print(type((3)))
# print(type((,)))
print(type((3,)))