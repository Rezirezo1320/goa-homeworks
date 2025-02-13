def no_duplicates(user_list):
    """ამოიღოს დუპლიკატები სიიდან და დააბრუნოს უნიკალური ელემენტების სია"""
    return list(set(user_list))  # set() ამოშლის დუპლიკატებს, ხოლო list() გადააქცევს ისევ სიად

# ფუნქციის გამოძახება სამჯერ სხვადასხვა არგუმენტებით
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = ["apple", "banana", "apple", "orange", "banana"]
list3 = [10, 20, 30, 10, 40, 20, 50]

print(no_duplicates(list1))  # [1, 2, 3, 4, 5]
print(no_duplicates(list2))  # ['apple', 'banana', 'orange']
print(no_duplicates(list3))  # [10, 20, 30, 40, 50]
