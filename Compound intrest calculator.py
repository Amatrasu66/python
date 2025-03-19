# this is a program to calculate the compound intrest of an amount or an compound intrest calculator

princ = 0
rate = 0
time = 0

while princ <= 0:
    princ = float(input("enter the principle amount : "))
    if(princ <= 0):
            print("the principle cannot be 0 or less than zero")

while rate <= 0:
    rate = float(input("enter the rate amount : "))
    if(rate <= 0):
            print("the rate cannot be 0 or less than zero")

while time <= 0:
    time = float(input("enter the time amount : "))
    if(time <= 0):
        print("the time cannot be 0 or less than zero"),

print("The principle amount is : ",princ)
print("The rate amount is : ",rate)
print("The time amount is : ",time)

amt = princ*pow(1+rate/100,time)

print("The compound intrest amount is provided below : ",amt)
