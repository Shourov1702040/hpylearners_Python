print("WELCOME TO LEAP YEAR CALCULATOR")

Y = int(input("Enter your year="))

A = Y%4
B = Y%400
C = Y%100
if C==0 and B==0:
    print("This year is leap year")

elif ((C!=0) and (A==0)):
    print("This year is leap year")

else:
    print("This year is not leap year")
