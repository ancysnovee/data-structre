class stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def printll(self):
        return self.items

if __name__=='__main__':
    c1=stack()
    c1.push(34)
    c1.push(56)
    print(c1.printll())
    
