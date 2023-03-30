print("HelloWorld!!")
print("Hello World!!, This is Sakshi Bandral!")
class person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def showinfo(self):
        print("name",self.name)
        print("age",self.age)
        return
p1=person("sakshi",45)
p1.showinfo()