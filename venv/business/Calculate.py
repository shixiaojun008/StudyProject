#def sum(m,n):
#    return  m+n

class Calculate:
    x = 0
    y = 0

    def __init__(self, xValue, yValue):
        self.x = xValue
        self.y = yValue

    def sum(self):
        return self.x + self.y


'''
cal = Calculate(5,6)
print(cal.sum())
'''