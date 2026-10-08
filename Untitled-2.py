a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a%2==0 and b%2==0:
    print("Both numbers are even.")
elif a%2==0 or b%2!=0:
    print("One number is even and the other is odd.")
