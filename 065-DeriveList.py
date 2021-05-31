# 列表推导式

list10 = [x for x in range(1,5)]
print (list10)

list12 = [x*2 for x in range(1,5)]
print (list12)

list13 = [x*2 for x in range(1,50) if x%5==0]
print (list13)

cells  = [(row,col) for row in range(1,5) for col in range(1,5)]
for cell in cells:
    print(cell, end="\t")

print("\n")

#字典推导式

my_text = "i love you, i love sxt, i love jerry"

char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

print("\n")

#集合推导式

list30 = {x for x in range(1,50) if x%5==0}
print (sorted(list30))

print("\n")

#生成器推导式 -- 生成元组


list40 = (x for x in range(1,50) if x%10==0)
print (sorted(list40))
print("\n")
print (sorted(list40))



