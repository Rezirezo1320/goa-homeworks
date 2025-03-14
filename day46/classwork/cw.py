def manual_list(start, end, step, user_num):
    return [num for num in range(start, end, step) if num > user_num]
print(manual_list(1, 20, 2, 10)) 
print(manual_list(5, 50, 5, 25))  
print(manual_list(10, 100, 10, 60)) 


numbers = [num for num in range(1, 101) if (num % 3 == 0) ^ (num % 5 == 0)]
print(numbers)

palindromes = [num for num in range(10, 201) if str(num) == str(num)[::-1]]
print(palindromes)
