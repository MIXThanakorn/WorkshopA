print("โปรแกรมคำนวนค่าเฉลี่ยคะแนนสอบทั้ง 3 ครั้ง")
print("--------------------------------------------")
def inputnameandscore():
    stunumber = input("Studentnumber: ")
    stuname = input("Studentname: ")
    score1 = int(input("Score of test 01: "))
    score2 = int(input("Score of test 02: "))
    score3 = int(input("Score of test 03: "))
    return (stunumber, stuname, score1, score2,score3)

def calculate(score1, score2,score3):
    averagescore = float(score1 + score2 + score3)/3
    return averagescore

def show(stunumber, stuname, averagesocre):
    print(f"{stunumber} {stuname} have score {averagescore:.2f}")

stunumber,stuname, score1, score2,score3 = inputnameandscore()
averagescore = calculate(score1, score2, score3)
show(stunumber, stuname, averagescore)

