'''
Assignment No: 02 (A-01)
Assignment Title:
 Write a Python program that computes the net amount of a bank account b
 transaction log from console input. The transaction log format is shown
 100 W 200 (Withdrawal is not allowed if balance is going negative. Writ
 withdraw and deposit) D means deposit while W means withdrawal.
 Suppose the following input is supplied to the program:
 D 300, D 300 , W 200, D 100 Then, the output should be: 500
'''
def main():
    account=[]
    balance=0
    while True:
        print("1. Press 1 for log entry:")
        print("2. Press 2 for stop: ")
        ch=int(input("Enter your choice:"))
        if ch==1:
            log=input("Enter log:")
            account=(log.split())
            if account[0]=="D":
                balance+=int(account[1])
                print("Account credited by rs.",account[1])
                print("Current balance:",balance)
            elif account[0]=="W":
                if int(account[1])<int(balance):
                    balance-=int(account[1])
                    print("Account debited by rs.",account[1])
                    print("Current balance:",balance)
                else:
                    print("Insufficient balance")
        if ch==2:
            print("Thank you")
            break
main()