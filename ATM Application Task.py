#ATM APPLICATION
while True:
    accoount=10000
    card=input("insert the card")
    pwd=1234
    if card=="c":
        print("welcome nandu....")
        password=int(input("enter the password"))
        if password==pwd:
          option=int(input('''choose the option
                               1.balance enq
                               2.withdraw'''))
          if option==1:
             print("your acc bal is",account)
          elif option==2:
             money=int(input("enter the money"))
             print(money)
             balance("rem acc bal is",balance)
        else:
             print("Exit...")
             break
    else:
           print("incorrect password")
else:
            print("invalid card")
