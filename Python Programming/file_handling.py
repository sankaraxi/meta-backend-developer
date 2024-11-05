file = open("file_handling.txt", mode='r')

data = file.readlines()
print(data) 
file.close()

with open("file_handling.txt", mode='r') as main_file:
    data = main_file.readline()
    print(data)