print("โปรแกรมคำนวนเงินเดือนสุทธิของพนักงาน")
print("--------------------------------------------")
def inputnameandsalary():
    number = input("employee number: ")
    name = input("employee name: ")
    salary = int(input("salary: "))
    return number,name,salary

def calculate(number,name,salary):
    netsalary = salary - (salary*0.07) -500
    return netsalary

def show(number,name,salary,netsalary):
    print(f"{number} {name} have salary {salary} bath have netsalary {netsalary:.2f} bath")




number,name,salary = inputnameandsalary()
netsalary = calculate(number,name,salary)
show(number,name,salary,netsalary)
