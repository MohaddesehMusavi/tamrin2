from math import nextafter


number = int(input("Please Enter a number : "))
nex_number = ( number // 7 ) * 7 + 7
if number % 7 == 0 :
    print("number is multiple of 7 ")   
else :
    print("number is not multiple of 7 \n the next number is a multiple of 7 : ",nex_number)
    


