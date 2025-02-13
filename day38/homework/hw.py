# 1. შექმენით Set მინიმუმ 5 ელემენტით
my_set = {10, 20, 30, 40, 50}
print("Initial Set:", my_set)

# 2. დაამატეთ ახალი ელემენტი
my_set.add(60)
print("After Adding 60:", my_set)

# 3. წაშალეთ არსებული ელემენტი (მაგალითად, 30)
my_set.remove(30)  # remove() გამოიწვევს შეცდომას, თუ ელემენტი არ არსებობს
print("After Removing 30:", my_set)

# 4. შეამოწმეთ, შეიცავს თუ არა Set-ი კონკრეტულ მნიშვნელობას (მაგალითად, 40)
if 40 in my_set:
    print("40 is in the set")
else:
    print("40 is not in the set")



# ორი Set-ის შექმნა საერთო ელემენტებით
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# გაერთიანება (Union) - აერთიანებს ყველა უნიკალურ ელემენტს ორივე Set-იდან
union_set = set1.union(set2)
print("Union:", union_set)  # {1, 2, 3, 4,
