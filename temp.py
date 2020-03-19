selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

for x in selfref_list:
    print(x)

print(selfref_list)