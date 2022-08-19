win = 0
equal = 0
loss = 0
count = 1
score = 0
while count <= 8 :
    print("\n Please Enter the result of game",count,": \n    1)win \n    2)equal \n    3)loss" )
    number = int(input("result : "))
    print("________________________________________")
    if number == 1 :
        win += 1
        score += 3
    elif number == 2 :
        equal +=  1
        score += 1
    elif number == 3 :
        loss += 1
        score += 0
    else :
        print("Please select only from the options.")
        count -= 1
    count += 1


print("\n score : ",score ,"\n win : ",win , "\n equal : ",equal , "\n loss : ",loss)