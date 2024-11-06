

my_list = [1,2,3,4]

#Traditional function
print("Traditional function")
def add_one(item):
    return my_list.append(item)

new_list = add_one(5)
print(my_list)

#Pure function
print("Pure function")
def add_one_pure(item, my_list):
    new_list = my_list.copy()
    new_list.append(item)
    return new_list

new_list = add_one_pure(6, my_list)
print(my_list)
print(new_list)
