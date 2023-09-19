print("โปรแกรมคำนวนดอกเบี้ยเงินกู้")
print("--------------------------------------------")
def inputloan():
    name = input("Your name: ")
    loan = int(input("your loan: "))
    return name, loan


def process(name, loan):
    if loan > 1000 :
        x = loan*0.025
        return x
    else:
        y = loan*0.055
        return y


def show(x,y):
    if x :
        print(f"{name} your loan is {loan} bath and you have interes {x} bath")
    elif y :
        print(f"{name} your loan is {loan} bath and you have interes {y} bath")

name,loan = inputloan()
x = process(name, loan)
y = process(name, loan)
show(x,y)
