#str(start:stop:step)

def string_reversal(string):
    return string[::-1]

# print(string_reversal("Hello World!"))
# print(string_reversal("1234567890"))
# print(string_reversal("Python Programming"))

def string_reversal2(string):
    if len(string) == 0:
        return string
    else:
        return string_reversal2(string[1:]) + string[0]

print(string_reversal2("Hello World!"))
print(string_reversal2("1234567890"))
print(string_reversal2("Python Programming"))

