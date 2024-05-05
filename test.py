
class Test:
    def __init__(self,type, price):
        self.type=type
        self.price=price
    def __str__(self):
        return "Type: "+self.type+" Price: "+self.price
    

t=Test("a","b")
print(t.type)
print(t)


