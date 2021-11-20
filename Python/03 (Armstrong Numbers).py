number = input("Please enter a number: ")
string_num = number.isdigit()

while not string_num:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Try again: ")
    string_num = number.isdigit()

temp_num = int(number)
digit_num = 0

while temp_num > 0:
    digit_num += 1
    temp_num //= 10

sum = 0
temp_num = int(number)
while temp_num > 0:
    remainder = temp_num % 10
    sum += pow(remainder, digit_num)
    temp_num //= 10

if sum == int(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
