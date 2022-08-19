number = int(input("Please Enter a Number : "))
number1 = number
number2 = 0 
while number > 0 :
    number2 = (number2 * 10) + (number % 10)
    number = number //  10
print(" Reverse of number = ",number2)

if number1 == number2 :
    print("the number is equal to it's reverse . ")
else :
    print("the number is not equal to it's reverse . ")

