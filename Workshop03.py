print("โปรแกรมคำนวนภาษี")

def inputnameandprice():
    price = int(input("productprice: "))
    productname = input("productname: ")
    return price,productname

def calculate(price,productname):
    tax = price*0.07
    return tax

def show(price,productname,tax):
    print(f"product {productname} price is {price} bath tax {tax:.2f} bath")


price,productname = inputnameandprice()
tax = calculate(price,productname)
show(price,productname,tax)
