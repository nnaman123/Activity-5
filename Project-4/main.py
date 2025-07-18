#to check if the number is odd or even
num = int(input("Enter a number: "))
num2 = num % 2
if num2 == 0:
    print("The number is even")
else:
    print("The number is odd")