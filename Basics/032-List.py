
# list 的生成

#通过list 生成

#list1 = ["A", "B", "C"]
list1 = list("ABC")
print(list1)

#通过 range 生成
list2 =list(range(1, 50, 3))
print(list2)

#通过推导式生成列表

list3 =[x*2 for x in range(5)]
print (list3)

list1.append("JERRY")
print(list1)

list2.extend(["TOM", "GO"])
print(list2)


list10 = [20, 40, 60, 10, 90, 70]
list10.sort()
print(list10)
list11 = [20, 40, 60, 10, 90, 70]
list11.sort(reverse=True)
print(list11)


list20 = [20, 10, 40, 30]
reversedList20 = reversed(list20)
list21 = list(reversedList20)
print(list21)


list30 = [
    ["高小一",18,30000,"北京"],
    ["高小二",19,40000, "上海"],
    ["高小三",20,50000, "深圳"]
]

print(list30[1])

for x in range(3):
    print(list30[x])




'''
print ("var1[1:3]:", var1.capitalize()[0:3])
print(var1.isupper())

print(var1.zfill(20))

'''

'''
# 海象运算符号
a = "1234567890888"
n = 0
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
'''

'''
list1 = ["A", "B", "C"]
list2 = ["D", "E", "F", "E"]

print(list1 + list2)
list3 = list1.copy()
print(list3)

print("A" in list1)



list11 = [1, 5, 7, 8, 5, 3, 6]
list11.sort()
print(list11)


subjects = {"Chinese", "Math", "English", "Physic"}

for subject in subjects:
    if subject != "Math":
        print(subject, end=',')
print("\nFinish!")


for i in range(0,100,5):
    print(i,end=',')

'''









