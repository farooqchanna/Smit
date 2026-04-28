def view():
    try:
        with open("expense.csv","r") as file:
            val =[data.strip().split(",") for data in file.readlines()]
        return val
    except FileNotFoundError:
        print("No expense")
    except Exception as e:
        print(e)

def add(exp,amount):
    from datetime import date
    today = date.today()
    total = f"{today},{exp},{amount}\n"
    with open("expense.csv","a+") as file:
        file.write(total)
        print(file.read())

def cat(x):
    a = view()
    label = ["Date: ", "Expense: ","Amount: "]
    for data in a:
        if x== data[1]:
            print("*"*10)
            for i in range(len(label)):
                print(label[i],data[i])
            break
    else:
        print("No Expense Found")


def total():
    b = view()
    total = [int(data[2]) for data in b]
    print(f"Total Expense : {sum(total)}")

while True:
    try:
        sel = int(input("1. Add Expense:\n2. View Expense:\n3. Search by Catogary\n4. Total Expense:\n5. Exit:\n:"))
    except ValueError:
        print("Type only number between 1 to 4")
        continue
        
    if sel == 1:
        while True:
            try:
                exp = input("Enter your expense: ")
            except Exception as e:
                print(e)
                continue
            try:
                amount = int(input("enter your amount here: "))
            except  ValueError:
                print("type numerical amount")
                continue
            add(exp,amount)
            choice = input("Add another? (y/n): ").lower()
            if choice != 'y':
                break
    elif sel == 2:
        a= view()
        print(a)
    elif sel == 3:
        x= input("Enter your catogary: ")
        cat(x)
    elif sel == 4:
        total()
    elif sel == 5:
        print("thank you for using")
        break