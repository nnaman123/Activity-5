#cheking if a number is greater or smaller
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
elif first_number < second_number:
    print(f"{first_number} is smaller than {second_number}")
else:
    print(f"{first_number} is equal to {second_number}")
    