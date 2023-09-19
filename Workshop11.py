print("โปรแกรมคำนวนค่าโทร")

def inputphonenumberandtime():
    name = input("What's your name: ")
    phonenumber = input("what's your phonenumber: ")
    time = int(input("How much time do you spend on calls(Minute): "))
    return name,phonenumber,time

def process(name,phonenumber,time):
    if 1 <= time <= 15:
        x = f"{name} {phonenumber} you use {time} minutes to call you should pay {time*5} bath"
        return x
    elif 16 <= time <= 30:
        y = f"{name} {phonenumber} you use {time} minutes to call you should pay {time*3} bath"
        return y
    elif time >= 31:
        z = f"{name} {phonenumber} you use {time} minutes to call you should pay {time*1.5:.2f} bath"
        return z

def show(x,y,z):
    if x:
        print(x)
    elif y:
        print(y)
    else:
        print(z)

name,phonenumber,time = inputphonenumberandtime()
x = process(name,phonenumber,time)
y = process(name,phonenumber,time)
z = process(name,phonenumber,time)
show(x,y,z)