def sum_of_nums(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum += value
    return round(sum,2)

print(sum_of_nums(coffee=25.532, tea=15.523, juice=10.523)) # 51.5
print(sum_of_nums(coffee=25.532, tea=15.523)) # 41.05
print(sum_of_nums(coffee=25.532)) # 25.53

