try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Error: That is not a valid number.")

my_list = [1, 2, 3]

try:
    print(my_list[5])  # არარსებული ინდექსი
except IndexError:
    print("Error: Index out of range.")
