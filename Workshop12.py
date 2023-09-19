print("โปรแกรมคำนวนค่าใช้จ่ายในการซื้อแพ็กเกจกการท่องเที่ยว")

def inputinformation():
    name = input("Tour leader name: ")
    phonenumber = input("Tour leader phonenumber: ")
    people = int(input("How many tourists: "))
    return name, people, phonenumber

def process(name, people, phonenumber):
    if people <= 2 :
        a = f"Tour leader {name} Tel.{phonenumber} number of tourists {people} Total cost {people*300} bath"
        return a
    elif 3 <= people <= 5:
        b = f"Tour leader {name} Tel.{phonenumber} number of tourists {people} Total cost {people*250} bath"
        return b
    elif 6 <= people <= 10:
        c = f"Tour leader {name} Tel.{phonenumber} number of tourists {people} Total cost {people*210} bath"
        return c
    elif people >= 11: 
        d = f"Tour leader {name} Tel.{phonenumber} number of tourists {people} Total cost {people*150} bath"
        return d

def show(a,b,c,d):
    if a:
        print(a)
    elif b :
        print(b)
    elif c :
        print(c)
    else:
        print(d)

name, people, phonenumber = inputinformation()
a = process(name, people, phonenumber)
b = process(name, people, phonenumber)
c = process(name, people, phonenumber)
d = process(name, people, phonenumber)
show(a,b,c,d)