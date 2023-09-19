print("Bingo game!!")
print("--------------------------------------------")
def inputnumber():
    number = int(input("Guess the number: "))
    return number

def process(number):
    if number == 25 :
        x = "Correct, You are the winner"
        return x
    else:
        y = "Not Correct !!!."
        return y

def show(x,y):
    if x :
        print(x)
    elif y:
        print(y)

number = inputnumber()
x = process(number)
y = process(number)
show(x,y)
