import json
# One JSON file contains a list of dictionaries (account info) of all users in the bank
file = open("bank.json","r")
users = json.load(file)
file.close()

######

# If there is no users yet make the user type sign Up without asking him whether if he has an account or not
ID=0
if len(users) == 0:
    z = 0
    while z == 0:
        acc = input("There are No Accounts yet, type 'Sign Up'\n")
        if acc == "Sign Up" or acc == "Sign up" or acc == "sign Up" or acc == "sign up":
            name = input("please enter your NAME :- (in this Format NAME1 NAME2) ")
            while 1:    #loop le7ad ma yeda5al el esm sona2y bas s7 men 8ir arkam
                l = name.split()
                if len(l) != 2 or not l[0].isalpha() or not l[1].isalpha():   #yet2aked el esm sona2y we en kol wahed fihom 7erof bas
                    print("Enter a valid name please")
                    name = input("please enter your NAME again :- ")
                else:
                    break

            password = input("please enter your PASSWORD :- ")
            while 1:  #loop le7ad ma yeda5al el pass s7 men 8ir ay space law da5al space error we yeda5al tany
                l = password.split()
                if len(l) != 1: # 3shan ay password bib2a kelma wahda flaw 3amlna split we tl3 list fiha aktar men kelma yeb2a ya5od tany
                    password = input("please enter a valid PASSWORD :- ")
                else:
                    break #3shan law s7 yetla3

            phonenum = input("please enter your PHONE NUMBER :- ")
            while 1:     #loop le7ad ma yeda5al el number s7 men 8ir 7eroof law da5al 7arf error we yeda5al tany
                if not phonenum.isdigit():
                    phonenum = input("please enter a valid phone number please")
                else:
                    break  #3shan law s7 yetla3
            mail = input("please enter your MAIL :- ")
            while 1:  #loop le7ad ma yeda5al el mail s7 men 8ir space law da5al space error we yeda5al tany
                l = mail.split()
                if len(l) != 1:
                    mail = input("ENTER A VALID Mail PLEASE :- ")
                else:
                    break
            gender = input("please enter your GENDER :- ")
            while 1:  #loop le7ad ma yeda5al kelma mail aw femail law ay kelma tanya error we yeda5al tany
                l = gender.split()
                if len(l) != 1:
                    gender = input("please enter a valid GENDER :- ")
                elif gender.lower() == "male" or gender.lower() == "female":
                    if gender.lower() == "male":
                        gender = "Male"
                    else:
                        gender = "Female"
                    break
                else:
                    gender = input("please enter a valid GENDER :- ")

            age = input("please enter your AGE :- ")
            while 1:   #loop le7ad ma yeda5al arkam bs law da5al 7eroof aw psace erorr we yeda5al tany
                if not age.isdigit():
                    age = input("please enter a valid age please")
                else:
                    break
            city = input("please enter your CITY :- ")
            while 1:
                if city.isdigit():   #loop le7ad ma yeda5al ay haga 8ir arkam law da5al arkam bs error
                    city = input("Enter a valid city please")
                else:
                    break
            addacc = {
                "name": name,
                "password": password,
                "phone number": phonenum,
                "mail": mail,
                "gender": gender,
                "age": age,
                "city": city,
                "balance": 0
            }
            users.append(addacc)
            file = open("bank.json", "w")
            json.dump(users, file, indent=3)
            file.close()
            ID= len(users)-1
            print(f"Signed Up Successfully, Your ID is {ID}")
            break

        else:
            continue


# if there are accounts in the system ask the user if he wants to log in or sign up

elif len(users) != 0:
  while 1 :   # loop 3shan law da5al 7aga 8ir sign up aw log in yerga3 ya5od tany input we fi break law da5al s7
    acc = input("If you already have an account enter Log In \nIf you don't have an account enter Sign Up\n")
    if acc == "Sign Up" or acc == "Sign up" or acc == "sign Up" or acc == "sign up":
        print("*WELCOME TO SIGN UP PAGE*")
        name = input("please enter your NAME :- ")
        while 1:
            l = name.split()
            if len(l) != 2 or not l[0].isalpha() or not l[1].isalpha():
                print("Enter a valid name please")
                name = input("please enter your NAME :- ")
            else:
                break

        password = input("please enter your PASSWORD :- ")
        while 1:
            l = password.split()
            if len(l) != 1:
                print("ENTER A VALID PASSWORD PLEASE ")
                password = input("please enter your PASSWORD :- ")
            else:
                break

        phonenum = input("please enter your PHONE NUMBER :- ")
        while 1:
            if not phonenum.isdigit():
                phonenum = input("please enter a valid phone number please")
            else:
                break
        mail = input("please enter your MAIL :- ")
        while 1:
            l = mail.split()
            if len(l) != 1:
                mail = input("ENTER A VALID Mail PLEASE :- ")
            else:
                break
        gender = input("please enter your GENDER :- ")
        while 1:
            l = gender.split()
            if len(l) != 1:
                gender = input("please enter a valid GENDER :- ")
            elif gender.lower() == "male" or gender.lower() == "female":
                if gender.lower() == "male":
                    gender = "Male"
                else:
                    gender = "Female"
                break
            else:
                gender = input("please enter a valid GENDER :- ")

        age = input("please enter your AGE :- ")
        while 1:
            if not age.isdigit():
                age = input("please enter a valid age please")
            else:
                break
        city = input("please enter your CITY :- ")
        while 1:
            if city.isdigit():
                city = input("Enter a valid city please")
            else:
                break
        addacc = {
            "name": name,
            "password": password,
            "phone number": phonenum,
            "mail": mail,
            "gender": gender,
            "age": age,
            "city": city,
            "balance": 0
        }
        users.append(addacc)
        file = open("bank.json", "w")
        json.dump(users, file, indent=3)
        file.close()
        ID = len(users) - 1
        print(f"Signed Up Successfully, Your ID is {ID}")
        break

    elif acc == "Log In" or acc == "Log in" or acc == "log In" or acc == "log in":
        f = 0
        while f == 0:
            print("*WELCOME TO LOG IN PAGE*")
            ID = input("Please enter your ID ")
            z = 0                                                         # loop le7ad ma yeda5al el id s7 msh 7errof we in range
            while z == 0:
                if not ID.isdigit() or int(ID) not in range (len(users)):
                    print("Your ID is not valid, Try again ")
                    ID = input("Please enter your ID ")
                else:
                    ID=int(ID)
                    z = 1

            password = input("Please enter your password: ")
            if password != users[ID]["password"]:
                for i in range (2):
                        print("Your password is not correct, Try again ")
                        password = input("Please enter your password: ")
                        if password == users[ID]["password"]:
                            break
                        else:
                            print("***** Too many failed tries *****")



            if ID in range (len(users)) and password == users[ID]["password"]:
                out1, out2 = users[ID]['name'].split()
                z = out1[0:1].upper() + out1[1:] + " " + out2[0:1].upper() + out2[1:]  # 3shan netba3 awl 7araf men kol esm capitall
                print(f"WELCOME BACK, {z}!")
                f = 1

        break

    else :
        continue


balance = 0    #balance of the user

y = 0
while y == 0 : # loop until the user chooses to exit the program

# Menu:
    out1, out2 = users[ID]['name'].split()
    z = out1[0:1].upper() + out1[1:] + " " + out2[0:1].upper() + out2[1:]  # 3shan netba3 awl 7araf men kol esm capitall slicing le awl 7arf fe kol esm mn el esm el sona2y n3ml le awl 7arf upper

    print(f"★★★ WELCOME TO THE LIST OF OPTIONS, {z} ★★★")
    choice = input("Please enter your choice: \n [0] Deposit \n [1] Withdraw \n [2] Transfer \n "
                       "[3] Check your Balance & Personal Info \n [4] Exit \n" )

#Deposit:
    if choice == "0":
        balance = users[ID]["balance"]
        amount = input("Please enter the amount you want to deposit and the currency in this format: '# EGP' \n")
        l1 = amount.split(" ")
        while 1 :
            if len(l1) != 2 or not l1[0].isdigit() or int(l1[0])<=0:
                amount = input("INVALID INPUT enter it again ")
                l1 = amount.split()
                continue
            elif l1[1].upper() !="SAR" and l1[1].upper() !="USD" and l1[1].upper() !="EGP" :
                amount = input("INVALID INPUT enter it again ")
                l1 = amount.split()
                continue
            else :
                break
        l1[1]=l1[1].upper()
        if l1[1] == "USD":
            amount = int(l1[0])
            deposit = amount * 30
            balance += deposit
            users[ID]["balance"] = balance
            print(f"{amount} USD was deposited successfully!\nYour Balance is : {balance} EGP")
        elif l1[1] == "SAR":
            amount = int(l1[0])
            deposit = amount * 9
            balance += deposit
            users[ID]["balance"] = balance
            print(f"{amount} SAR was deposited successfully!\nYour Balance is : {balance} EGP")
        elif l1[1] == "EGP":
            amount = int(l1[0])
            deposit = amount
            balance += deposit
            users[ID]["balance"] = balance
            print(f"{amount} EGP was deposited successfully!\nYour Balance is : {balance} EGP")
        else:
            print("The currency you entered is not available, Try again")


        file = open("bank.json", "w")
        json.dump(users, file, indent=3)
        file.close()
        y = int(input("If you want to continue type 0, if you want to exit type 1 "))

# Withdraw

    elif choice == "1":
        while 1:
            s = input("Please enter the amount you want to withdraw and the currency in this format: '# CURRENCY': ")
            money = s.split()
            while True:  # loop le7ad ma yeda5al amount mawgood 3nd el sender
                if len(money) != 2 or not money[0].isdigit() or len(money[1]) != 3 or int(money[0]) <= 0:
                    s = input("INVALID INPUT enter it again ")
                    money = s.split()
                    continue
                elif money[1].upper() != "SAR" and money[1].upper() != "USD" and money[1].upper() != "EGP":
                    s = input("INVALID INPUT enter it again ")
                    money = s.split()
                    continue
                else:
                    break

            amount, currency = s.split()
            currency=currency.upper()
            amount = int(amount)

            if currency == "USD":
                amount *= 30
            elif currency == "SAR":
                amount *= 9

            if amount <= users[ID]['balance']:
                users[ID]['balance'] -= amount
                print(f"{amount} EGP was withdrawn successfully!\nYour new balance is: {users[ID]['balance']} EGP")

                file = open("bank.json", "w")
                json.dump(users, file, indent=3)
                file.close()
                break
            else:
                print("INSUFFICIENT FUNDS.")
                m = input("to re-enter the amount press 1.to exit press 0")
                if m == "1" :
                    continue
                else :
                    break


# Transfer
    elif choice == "2":
      while 1:
            print("---------TRANSFER-------")
            k=1
            acc2 = input("ENTER THE RECEIVER'S ID PLEASE. : - ")
            while True:  # loop le7ad ma yeda5al id s7

                if not acc2.isdigit() or int(acc2) >= len(users) or int(acc2) == ID: #law el id msh felrange aw haye3mel transfer lenafso
                    print("ID NOT FOUND, PRESS 1 TO ENTER IT AGAIN PRESS 0 TO RETURN TO THE MENU :- ")

                    while 1:  # loop le7ad ma yeda5al rakam 0 aw 1
                        x = input("")
                        if x == "1":
                            k = 1
                            break
                        elif x == "0":
                            k = 0
                            break
                        else:
                            print("ENTER A VALID CHOICE PLEASE :- ")
                    if k == 0:
                        break
                    acc2 = input("ENTER THE RECEIVER ID PLEASE : - ")
                else:
                    break

            if k == 0:
                break
            acc1 = ID
            acc2 = int(acc2)
            k = 1
            s = input(f"ENTER THE AMOUNT TO BE TRANSFERRED FROM  user {ID} to user {acc2} :-  ")
            money = s.split()

            while True:  # loop le7ad ma yeda5al amount mawgood 3nd el sender
                if len(money) != 2 or not money[0].isdigit() or len(money[1]) != 3:
                    s = input("INVALID INPUT enter it again ")
                    money = s.split()
                    continue
                amount, currency = s.split()
                currency = currency.upper()
                amount = int(amount)
                if currency == "USD":
                    amount *= 30
                elif currency == "SAR":
                    amount *= 9
                elif currency == "EGP":
                    amount = amount
                else:
                    s = input("INVALID INPUT enter it again ")
                    money = s.split()
                    continue
                if amount > users[ID]["balance"] or amount <= 0:
                    print("INSUFFICIENT AMOUNT OF MONEY , PRESS 1 TO ENTER IT AGAIN PRESS 0 TO RETURN TO THE MENU :- ")
                    k = 0
                    while 1:  # loop le7ad ma yeda5al rakam 0 aw 1
                        x = input("")
                        if x == "1":
                            k = 1
                            break
                        elif x == "0":
                            k = 0
                            break
                        else:
                            print("ENTER A VALID CHOICE PLEASE :- ")
                    if k == 0:
                        break
                    s = input(f"ENTER THE AMOUNT TO BE TRANSFERRED FROM  {ID} to {acc2} :-  ")
                    money = s.split()

                else:
                    break
            if k == 0:
                break
            users[acc2]["balance"] += amount
            users[acc1]["balance"] -= amount
            file = open("bank.json", "w")
            json.dump(users, file, indent=3)
            file.close()
            print(f"TRANSFER DONE, Your balance is {users[acc1]['balance']}")
            x = int(input("TO TRANSFER AGAIN PRESS 1.TO RETURN TO THE MENU PRESS 0 :- "))
            if x == 1:
                continue
            else:
                break


# Account info
    elif choice == "3":
            print("-----Check your Balance & Personal Info------")
            acc = int(ID)
            print(f"ID : {acc}")
            out1,out2 =users[acc]['name'].split()
            z=out1[0:1].upper()+out1[1:]+" "+out2[0:1].upper()+out2[1:]    # 3shan netba3 awl 7araf men kol esm capitall
            print(f"Name : {z}")
            print(f"Phone number : {users[acc]['phone number']}")
            print(f"Mail : {users[acc]['mail']}")
            print(f"Gender : {users[acc]['gender']}")
            print(f"Age : {users[acc]['age']}")
            print(f"City : {users[acc]['city']}")
            print(f"Balance : {users[acc]['balance']}")
            y = int(input("If you want to continue type 0, if you want to exit type 1 "))


    # Exit
    elif choice == "4":
        out1, out2 = users[ID]['name'].split()
        z = out1[0:1].upper() + out1[1:] + " " + out2[0:1].upper() + out2[1:]
        print(f"THANK YOU, {z}!")
        break

    else :
        print("INVALID INPUT TRY AGAIN")

file = open("bank.json", "w")
json.dump(users, file)
file.close()
