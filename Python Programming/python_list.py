list_1 = [1,2,3,4,5]

print(list_1) # [1, 2, 3, 4, 5]
print(*list_1) # 1 2 3 4 5

list_2 = [6,7,8,9,10]

list_2.append(11)
print(list_2) # [6, 7, 8, 9, 10, 11]

list_1.insert(len(list_1), list_2)

print(list_1) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]] 

list_1.extend(list_2)

print(list_1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_1.count(1)) #1
print(list_1.index(10)) #10