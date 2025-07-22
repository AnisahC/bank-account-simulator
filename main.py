from checking_account import CheckingAccount

def main():
    myAccount = CheckingAccount("Anisah")
    myAccount.deposit(100)
    myAccount.deposit(150)
    myAccount.withdraw(1000)
    print(myAccount.name)

if __name__ == "__main__":
    main()