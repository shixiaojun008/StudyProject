# define a dictionary

dict1 = {'name':'Jerry','age':33,'job':'Manager'}

dict2 = {'name':'Tom','age':32, 'job':'Worker'}

dict3 = dict(name='Snoopy', age=28, job='Casher')

key = 'name'

print(dict1[key])
print(dict2.get(key))

print(dict2.keys())
print(dict2.values())

dict1['age'] = 36
dict1['address'] = 'Suzhou'
print(dict1)

a, b, c, d = dict1
l, m, n, k = dict1.values()

print(a, b, c, d, l, m, n, k)

dict20 = [
    {"name":"高小一", "age":18, "salary":30000, "city":"北京"},
    {"name":"高小二", "age":19, "salary":40000, "city":"上海"},
    {"name":"高小三", "age":20, "salary":50000, "city":"深圳"}
]
print(dict20)
print(dict20[0])
print(dict20[1])

for x in range(3):
    print(dict20[x].get("salary"))

for x in range(len(dict20)):
    print(dict20[x].get("name"), dict20[x].get("age"), dict20[x].get("salary"), dict20[x].get("city"))






