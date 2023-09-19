print("โปรแกรมคำนวนค่าคอมมิชชั่น")
print("--------------------------------------------")
def inputnameandsales():
    number = input("employee number: ")
    name = input("employee name: ")
    sales = int(input("employee sales: "))
    return number,name,sales


def process(number,name,sales):
    if sales < 1000:
        a = f"{number} {name} sales {sales} bath You have no commision"
        return a
    elif 1001 <= sales <= 2000:
        b = f"{number} {name} sales {sales} bath You have commision for {sales*0.01} bath"
        return b
    elif 2001 <= sales <= 3000:
        c = f"{number} {name} sales {sales} bath You have commision for {sales*0.03} bath"
        return c
    elif sales > 3001:
         d = f"{number} {name} sales {sales} bath You have commision for {sales*0.05} bath"
         return d

def show(a,b,c,d):
    if a:
        print (a)
    elif b: 
        print (b)
    elif c:
        print(c)
    elif d:
        print(d)

number,name,sales = inputnameandsales()
a = process(number,name,sales)
b = process(number,name,sales)
c = process(number,name,sales)
d = process(number,name,sales)
show(a,b,c,d)