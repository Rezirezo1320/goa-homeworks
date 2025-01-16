name=str(input("enter name: "))

choice = input("Enter your choice ('u' for uppercase, 'l' for lowercase): ")

if choice == "u":
  print(name.upper())
elif choice == "l":
  print(name.lower())
else:
    print("Wrong information") 



def manual_find(main_string, str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i + len(str_to_find)] == str_to_find:
            return i



#საკლასო დავალება:

#მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.
#შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_count ცვლადში.
#დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში

main_str=str(input("enter str: "))
str_to_count =str(input("enter str2: "))
print(main_str.count(str_to_count))


#საკლასო დავალება:
#შექმენით ფუნქცია სახელად manual_swapcase
def manual_swapcase(REzi_Var):
  ter =""
  for char in REzi_Var:
    if char.islower():ter+=char.upper()
    else: ter+=char.lower()