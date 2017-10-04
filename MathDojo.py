class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) is int or type(i) is float:
                self.result += i
            else:
                for j in i:
                    self.result += j
        return self
    def subtract(self, *args):
        for i in args:
            if type(i) is int or type(i) is float:
                self.result -= i
            else:
                for j in i:
                    self.result -= j
        return self

dojo = MathDojo()
print dojo.add(2).add(2,5).subtract(3,2).result
dojo.subtract(4)
print dojo.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result