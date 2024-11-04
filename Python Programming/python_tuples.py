my_tuple1 = (1, 21.5, "Python", "Programming", 5)

print(my_tuple1) # (1, 21.5, 'Python', 'Programming', 5)

print(my_tuple1[0]) # 1
print(my_tuple1[1]) # 21.5
print(my_tuple1[2]) # Python

print(my_tuple1.index("Programming")) # 3
print(my_tuple1.count(5)) # 1

for item in my_tuple1:
    print(item)