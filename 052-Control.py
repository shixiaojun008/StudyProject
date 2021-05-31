num1 = 10
#num = input("Please input a number:")
if int(num1)  == 10:
    print(num1)

num2 = 1000
print("number is smaller than 100" if int(num2) < 100 else "number is bigger than 100." )

num3 = 100

if int(num3) < 10:
    print("num3 is smaller than 10")
elif int(num3) < 100:
    print("num3 is smaller than 100")
else:
    print("num3 is bigger than 100")


score = 87
degree ="ABCDE"
number = 0

if 0 <= score <= 100:
    number = score//10
    if number < 6:
        number = 5
    print(degree[9-number])



sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(101):
    sum_all += x
    if x%2 == 1:
        sum_odd += x
    if x%2 == 0:
        sum_even +=x
print(sum_all,sum_odd, sum_even)

sum_odd2 = 0
for x in range(1,101,2):
    sum_odd2 += x
print(sum_odd2)


''' 打印9*9乘法口诀表 '''
for m in range(1,10):
    for n in range(1, int(m)+1):
        print ("{0}*{1}={2}".format(n, m, m*n), end="\t")
    print()
print()

list = [
    {"name":"高小一", "age":18, "salary":30000, "city":"北京"},
    {"name":"高小二", "age":19, "salary":40000, "city":"上海"},
    {"name":"高小三", "age":20, "salary":50000, "city":"深圳"}
]

for m in list:
    if (m.get("name") != "高小二" ):
        for n in m.values():
            print(n,end="\t")
        print()


names = ("Jerry10","Jerry12","Jerry14","Jerry16")
ages = (18,20,22,23)
jobs = ("Casher", "Farmer", "Workder", "Banker")

for name,age,job in zip(names, ages, jobs):
    print("{0} ** {1} ** {2}".format(name, age, job))

print()

for i in range(3):
    print("{0} ** {1} ** {2}".format(names[i], ages[i], jobs[i]))











