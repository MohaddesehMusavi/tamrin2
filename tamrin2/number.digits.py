Number = int (input("Please Enter a Namber : "))
even_digits = 0
odd_digits  = 0
while Number > 0 :
    temp = Number % 10
    Number = Number // 10
    if temp % 2 == 0 :
        even_digits += 1
    else :
        odd_digits += 1
if even_digits == odd_digits :
    print(" even digits = odd digits")
elif even_digits > odd_digits :
    print(" even digits > odd digits")
else :
    print(" even digits < odd digits")


