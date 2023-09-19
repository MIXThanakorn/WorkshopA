print("จงหาค่า y โดย y = 2x^2+ 2x + 1 ")

def inputx():
    x = int(input("Type X: "))
    return x

def Solveequation(x):
    y = (2*(x**2)) + (2*(x)) + 1
    return y


def show(x,y):
    print(f"If x = {x} Then y = {y}")

x = inputx()
y = Solveequation(x)
show(x,y)