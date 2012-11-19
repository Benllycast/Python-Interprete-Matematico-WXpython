# To change this template, choose Tools | Templates
# and open the template in the editor.

class Stack ():
    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.items = []

    def push(self, item):
        print self.nombre+" item: "+str(item)
        self.items.append(item)

    def pop(self):
        return (self.items.pop())

    def isEmpty(self):
        return (len(self.items)== 0)

    def peek(self):
        return (self.items[-1])

    def len(self):
        return (len(self.items))