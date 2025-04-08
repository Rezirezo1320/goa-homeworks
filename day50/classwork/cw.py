# ინტეჯერის ცვლადი
x = 10

try:
    # შეგნებულად ვცდილობთ ინტეჯერს "გავაწებოთ" სტრინგი, რაც გამოიწვევს TypeError-ს
    result = x + "abc"
except TypeError as e:
    print("TypeError აღმოჩენილია:", e)


try:
    user_input = input("შეიყვანე სახელი ან გვარი: ")
    
    # მაგალითად, აქ შეგნებულად ვცადოთ ინტეჯერში გადაყვანა, რაც გამოიწვევს ValueError-ს არასწორი ტიპის შემთხვევაში
    number = int(user_input)

except ValueError as ve:
    print("დაფიქსირდა ValueError:", ve)
except TypeError as te:
    print("დაფიქსირდა TypeError:", te)
except NameError as ne:
    print("დაფიქსირდა NameError:", ne)
except ZeroDivisionError as ze:
    print("დაფიქსირდა ZeroDivisionError:", ze)
except IndexError as ie:
    print("დაფიქსირდა IndexError:", ie)
except KeyError as ke:
    print("დაფიქსირდა KeyError:", ke)
except Exception as e:
    print("დაფიქსირდა გაუთვალისწინებელი შეცდომა:", e)
