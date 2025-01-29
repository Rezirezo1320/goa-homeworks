
#საკლასო დავალება:
#შექმენით ფუნქცია სახელად generate_big_sentence, რომელსაც გადაეცემა 3 პარამეტრი - name, surname, age.
#ფუნქციამ უნდა გამოგვიტანოს წინადადება ზუსტად იგივე წყობით, როგორც მე დავწერე (გადახედეთ რესურებს), გამოიყენეთ format ფუნქცია.
#სანამ ფუნქციას გამოიძახებთ, მომხმარებელს შემოატანინეთ ტერმინალიდან სახელი, გვარი, ასაკი და შეინახეთ ისინი ცვლადებში.
#ფუნქციის გამოძახებისას, მას არგუმენტებად უნდა გადაეცეს ეს ცვლადები

def generate_big_sentense( name, surname, age):
    name=str(input("entre name: "))
    surname=str(input("entre surname: "))
    age=str(input("entre age: "))

    print(f"hello,my name is {name}, my surname is {surname} and my age is {age}.")


#საკლასო დავალება:

#შექმენით ფუნქცია სახელად my_split, რომელსაც გადაეცემა ორი პარამეტრი - main_string და string_to_split.
#ფუნქციამ უნდა დაბეჭდოს სია - main_string გაიხლიჩოს string_to_split-ის მიხედვით.
#ფუნქციის გამოძახებამდე მომხარებელს შემოატანინეთ მთავარი და დასაყოფი სთრინგები,
#შეინახეთ ცვლადებში. შემდეგ გამოიძახეთ ფუნქცია და ეს ცვლადები გადაეცით არგუმენტებად
    def my_split(main_string,string_to_spling):
         print(main_string.split(string_to_spling))
         main=input("enter main string:")
         second=input("enter second string:")
         my_split(main,second)




def manual_append( main_list, item_to_insert):
     len=len(main_list)
     main_list.insert( len,item_to_insert)
     print(main_list)
