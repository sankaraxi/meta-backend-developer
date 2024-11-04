def sum_of_nums(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_of_nums(1,2,3,4,5)) # 15
print(sum_of_nums(1,2,3)) # 6