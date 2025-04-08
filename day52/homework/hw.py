def powers_of_two(n):
    res = []
    
    for i in range(n+1): res.append(2**i)
    
    return res
def powers_of_two(n):
    return [2**i for i in range(n+1)]