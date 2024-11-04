my_dict = {1:'21AIB31', 'Name': 'Sankar', 'Age': 21, 'Course': 'B.Tech'}

print(my_dict) # {1: '21AIB31', 'Name': 'Sankar', 'Age': 21, 'Course': 'B.Tech'}

print(my_dict[1]) # 21AIB31
print(my_dict['Name']) # Sankar

del my_dict['Age']
print(my_dict) # {1: '21AIB31', 'Name': 'Sankar', 'Course': 'B.Tech'}

my_dict['Age'] = 21
print(my_dict) # {1: '21AIB31', 'Name': 'Sankar', 'Course': 'B.Tech', 'Age': 21}
my_dict['College'] = 'KGISL'
print(my_dict) # {1: '21AIB31', 'Name': 'Sankar', 'Course': 'B.Tech', 'Age': 21, 'College': 'KGISL'}

print(my_dict.keys()) # dict_keys([1, 'Name', 'Course', 'Age', 'College'])
print(my_dict.values()) # dict_values(['21AIB31', 'Sankar', 'B.Tech', 21, 'KGISL'])

for key,value in my_dict.items():
    print(str(key) + " "+ str(value))