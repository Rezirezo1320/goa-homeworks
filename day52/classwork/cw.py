def get_average(marks):
    return int(sum(marks) / len(marks))



def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]