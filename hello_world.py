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


class bottel:
    def  __init__(self,material,colour,quality):
        self.material=material
        self.colour=colour
        self.quality=quality
        return
    def  info(self):
        print("material",self.material)
        print("colour",self.colour)
        print("quality",self.quality)
        return
b1=bottel("steel","silver","high")
b1.info()


# find the prime number:
x=98
y=34
if x>y:
    print("prime number")
else:
    print("not prime number")

# find even number:
u=66
if u%2==0&u%2!=1:
    print("even number")
else:
    print("not even number")

class table:
    def __init__(self,material,colour):
        self.material=material
        self.colour=colour
    def showinfo(self):
        print("material",self.material)
        print('colour',self.colour)
        return
c1=table('wood','brown')
c1.showinfo

# prime number:
n=int(input("enter the numbner"))
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**.5)+1):
        if n%2==0:
            return False
        return True
if is_prime(n):
    print("prime number")
else:
    ("not prime number")

