def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        prev_num = arr[i-1]
        
        if cur_num - prev_num > 1: return cur_num
    
    return None



def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")