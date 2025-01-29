def my_split(main_string,string_to_spling):
         print(main_string.split(string_to_spling))
         main=input("enter main string:")
         second=input("enter second string:")
         my_split(main,second)


#შექმენით ფუნქცია სახელად manual_append. ამ ფუნქციამ სიის ბოლოში უნდა ჩაამატოს ახალი ელემენტი.
#რ გამოიყენოთ append, გამოიყენეთ insert.
#ფუნქციას ექნება 2 პარამეტრი - main_list, item_to_insert.z

def manual_append( main_list, item_to_insert):
     len=len(main_list)
     main_list.insert( len,item_to_insert)
     print(main_list)



list1=[y,u,i,o,p,o,i,u,y]
print("[]".join(list1))