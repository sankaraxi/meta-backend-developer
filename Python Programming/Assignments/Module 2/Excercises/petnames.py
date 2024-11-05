f = open("petnames.txt", "r") # r can be omitted as it is the default mode

f_content = f.read()
# print(f_content)

f_content_list = f_content.split("\n")
# print(f_content_list)

f.close()
import random

def generate_name():
    return random.choice(f_content_list)

print(generate_name())