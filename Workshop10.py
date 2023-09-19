print("โปรแกรมแสดงข้อความต้อนรับ")
print("--------------------------------------------")
def inputnameandyear():
    name = input("What's your name: ")
    year = int(input("What year are you in (only1-4): "))
    return name, year

def process(name, year):
    if year == 1:
        a = f"hi {name} Welcome Freshman"
        return a
    elif year == 2:
        b = f"hi {name} Welcome Sophomore"
        return b
    elif year == 3:
        c = f"hi {name} Welcome Junior"
        return c
    elif year == 4:
        d = f"hi {name} Welcome Senior" 
        return d

def show(a,b,c,d):
    if a :
        print (a)
    elif b :
        print(b)
    elif c:
        print(c)
    else:
        print (d)


name,year = inputnameandyear()
a = process(name, year)
b = process(name, year)
c = process(name, year)
d = process(name, year)
show(a,b,c,d)
