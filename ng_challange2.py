n= input("Enter the initial unit for temeperature, c for celcius, k for kelvin, and f for farenheit: ")
m= input("Enter the unit of temperature you would like to convert to, c for celcius, k for kelvin, and f for farenheit: ")
while True:
    try:
        t= float(input("Enter the temperature you would like to convert: "))
        break
    except ValueError:
        print("The value you enter is not a number, please try again")

def temp_converter(n,m,t):
    if n=="c" or n=="C":
        if m=="k" or m=="K":
            temp = t+273.15
        if m=="f" or m=="F":
            temp = (t*9/5)+32
    if n=="k" or n=="K":
        if m=="c" or m=="C":
            temp= t-273.15
        if m=="f" or m=="F":
            temp= (t-273.15)*(9/5) +32
    if n=="f" or n=="F":
        if m=="c" or m=="C":
            temp = (t-32) *5/9
        if m=="k" or m=="K":
            temp = (t-32) *(5/9)+273.15
    print(temp)

temp_converter(n,m,t)
