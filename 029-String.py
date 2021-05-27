# ^，<，>分别代表居中，左对齐，右对齐
string1 = "我是{name}, 我喜欢数字:{number:*^8}"
print(string1.format(name="JERRY", number="0512"))

string2 = "我是{name}, 我喜欢数字:{number:*<8}"
print(string2.format(name="JERRY", number="0512"))

string3 = "我是{name}, 我喜欢数字:{number:*>8}"
print(string3.format(name="JERRY", number="0512"))

string4 = "我是：{name}, 我的存款有:{amount:.2f}元"
print(string4.format(name='JERRY', amount=120.898999))





