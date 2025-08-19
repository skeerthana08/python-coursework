data={'current balance': 6000,'history':[]}
def Menu():
    print('[C]heck Balance')
    print('[D]eposite')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit')
def Welcome():
    print('   WELCOME TO ATM    '.center(50,'='))
def Check_Balance():
    print(f'Current Balance : ${data["current balance"]}')
def Withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=data['current balance']:
        data['current balance']-=amount
        data['history'].append(f'Withdraw:${amount}')
        print(f'${amount} IS SUCCESSFULLY WITHDRAW !!!')
    else:
        print('INSUFFICIENT BALANCE')
def Deposit():
    amount=int(input("Enter the amount to deposit: "))
    data['current balance']+=amount
    data['history'].append(f'Deposit:${amount}')
    print(f'${amount} IS SUCCESSFULLY DEPOSITED !!!')
def View_History():
    if data['history']:
        print('TRANSATCION HISTORY'.center(40,'*'))
        for i in data['history']:
            print(i)
        else:
            print("NO TRANSACTION")
def Flow_Check(ch):
    if ch=='C':
        Check_Balance()
    elif ch=='D':
        Deposit()
    elif ch=='W':
        Withdraw()
    elif ch=='V':
        View_History()
    elif ch=='V':
        print( "  THANK YOU " . center(40,'*'))
    else:
        print(" INVALID CHOICE ")
    
Welcome()
while True:
    Menu()
    ch=input("Enter the char[CDWVE]: ").upper()
    Flow_Check(ch)