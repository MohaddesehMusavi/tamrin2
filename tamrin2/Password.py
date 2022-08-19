user_name = 99123123
password  = "Min_Mhddsh"
count = 0
for Pass in range (3) :
    User_name = int(input("Enter user name just three times:"))
    Password  = input("Enter password just three times :")

    if User_name == user_name and Password == password :
        print ("your welcome :)")
        break
    else :
        print("Please try again")
        count += 1
if count > 2 :
    print ("your Account has been locked :(")