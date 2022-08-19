Temperature = float(input("Please Enter Temperature :"))
print("Please select an option to change the temperature unit : \n  1) C--->F  \n  2) F--->C   \n  3) K--->F \n  4) F--->K  \n  5) C--->K \n  6) K--->C")
Selected_Number =input("which one selected?? : ")
if Selected_Number == '1' :
    fahrenheit = ( Temperature * 1.8 ) + 32
    print(fahrenheit," Fahrenheit")
elif Selected_Number == '2' :
    Celsius = (Temperature - 32) * (5 / 9)
    print(Celsius , " Celsius")
elif Selected_Number == '3' :
    fahrenheit = ( Temperature * 1.8 ) - 459.67
    print(fahrenheit," Fahrenheit")
elif Selected_Number == '4' :
    Kelvin = ( Temperature + 459.67 ) * (5 / 9) 
    print(Kelvin," Kelvin")
elif Selected_Number == '5' : 
    Kelvin = ( Temperature + 273.15 )  
    print(Kelvin," Kelvin")
elif Selected_Number == '6' :
    Celsius = (Temperature - 273.15) 
    print(Celsius , " Celsius")
else :
    print("Please select only from the options.")