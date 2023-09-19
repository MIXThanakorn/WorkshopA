print("โปรแกรมตรวจสอบค่า PH จากน้ำประปา")

def inputcityandPH():
    city = input("What is your city name: ")
    PH = int(input("How much PH in water: "))
    return(city,PH)

def process(city,PH):
    if 7 <= PH <= 8:
        x = f"{city} city Result is Normal"
        return x
    elif PH < 7 :
        y= f"{city} city Result is Alkali"
        return y
    elif PH > 8 :
        z = f"{city} city Result is Acid"
        return z

def show(x,y,z):
    if x:
        print(x)
    elif y :
        print(y)
    else:
        print(z)

city,PH = inputcityandPH()
x = process(city,PH)
y = process(city,PH)
z = process(city,PH)
show(x,y,z)

