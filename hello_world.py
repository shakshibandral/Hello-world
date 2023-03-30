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


class laptop:
    def  __init__(self,company,core,):
        self.core=core
        self.company=company
        return
    def detail(self):
        print("core",self.core)
        print("company",self.company)
        return
l1=laptop("i5","asus")
l1.detail()

# list:
a=["hii!!","how are you"]
print(type(a))
print(a)
a[1]="i am good"
print(a)