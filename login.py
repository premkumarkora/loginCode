import pandas as pd
print("CHOICES")
print("1.Login")
print("2.Register")
print("3.Forgot Password")
print("4.Exit")
choice=int(input("Let us know what you want to do now! "))
if choice == 1:
    loginnm= str(input())
    passwd=str(input())
    df = pd.read_csv("loginfo.csv")
    newdf = df[(df["login"] == loginnm) & (df["password"] ==  passwd)]
    if len(newdf.index) == 0:
        print("You have not registered with us, Request you to select 2 to register")

elif choice == 2:  # Register
    s = str(input("Please Enter a Valid eMail Id :: "))
    print("Password should contain  one Upper, One lower, one special Char and one number and length should be between 6 and 16 characters")
    password = str(input("Please Enter Your Password :: "))
    if s.count("@") == 1 and s.count(".") == 1:
        bet1 = s.index("@")
        bet2 = s.index(".")
        passupper = any(ele.isupper() for ele in password)
        passnumeric = any(ele.isnumeric() for ele in password)
        if s.count("@") == 1 and s.count(".") == 1 and len(s[bet1 + 1:bet2]) >= 4 and \
                s[0:1] in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") and \
                s[1:2] in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") and \
                s[2:3] in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") and \
                len(password) > 5 and len(password) < 16 and \
                passupper and passnumeric:
            filedata = open("loginfo.csv", "a")
            valuetowrite = s + "," + password + "\n"
            print(valuetowrite)
            filedata.write(valuetowrite)
            filedata.close()
            # print(bet1, bet2, s[bet1+1:bet2], s[0:1],s[1:2],s[2:3], s[-3:])
            print("Sucessfully created Login/ Password")
        else:
            print(
                "---Please check your Username/Password. Your User name shoule be a proper email id and password should contain one small case, one upper cse and a number")
    else:
        print("Please check your Username/Password. Your User name shoule be a proper email id and password should contain one small case, one upper cse and a number")




elif choice == 3: #Forgot Password
    import pandas as pd

    loginnm = str(input(" Please enter your eMail ID"))
    df = pd.read_csv("loginfo.csv")
    # print(df)
    newdf1 = df[(df["login"] == loginnm)]
    # print(newdf1.shape[0])
    # print("Size = ", newdf1.size)
    if newdf1.size < 2:
        print("You have not registered with us, Request you to select 1 to register")
    else:
        # print(newdf1["password"],  newdf1[(newdf1["password"] == loginnm)])
        print(" Your Password from our records is  :: ", newdf1.at[newdf1.index[0], 'password'])

else:
    print("Please select available choices")
