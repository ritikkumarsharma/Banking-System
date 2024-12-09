# Python Banking Program 

def show_balance(balance):
    print("**********************************************")
    print(f"Your balance is Rs {balance:.2f}") 
    print("**********************************************")
def deposit():
    print("**********************************************")
    amount = float(input("Enter an amount to be deposited ")) 
    print("**********************************************")
    if amount < 0:
        print("**********************************************")
        print("That's not a valid amount")
        print("**********************************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("**********************************************")
    amount = float(input("Enter amount to be withdraw: "))
    print("**********************************************")
    if amount > balance:
        print("**********************************************")
        print("insufficiant funds")
        print("**********************************************")
        return 0
    elif amount < 0:
        print("**********************************************")
        print("Amount must be greater than 0")
        print("**********************************************")
        return 0
    else:
        return amount
#def main():        
balance = 0
is_running = True

while is_running:
    print("**********************************************")
    print("                Banking Program               ")
    print("**********************************************")
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("**********************************************")
    Choice = input("Enter your choice (1-4): ")

    if Choice == '1':
        show_balance(balance)
    elif Choice == '2':
        balance += deposit()
    elif Choice == '3':
        balance -= withdraw(balance)
    elif Choice == '4':
        is_running = False
    else:
        print("**********************************************")
        print("That is not a valid choice ")
        print("**********************************************")
print("**********************************************")
print("Thank you! have a nice day ")
print("**********************************************")
#