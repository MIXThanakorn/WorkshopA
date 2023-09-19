print("โปรแกรมคำนวนราคาสินค้า")

def inputprice():
    price = int(input("productprice: "))
    productname = input("productname: ")
    return price,productname

def calculate(price,productname):
    realprice = price + (price*0.1)
    return realprice
    
def show(productname,realprice):
    print(f"product {productname} price is {realprice} bath")

price,productname = inputprice()
realprice = calculate(price,productname)
show(productname,realprice)



