s= "print('abcde')"

eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100, b=200)

# d1 = 30 	 d2 = 300
d1 = eval("a+b")
d2 = eval("a+b", dict1)

print("d1 = {0} \t d2 = {1}".format(d1, d2))
