
list_n = [12, 65, 54, 39, 102, 339, 221,]

result = list(filter(lambda x: (x % 13 == 0), list_n))

print("Numbers divisible by 13 are",result)