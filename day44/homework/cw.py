def multiply(n):
    num_digits = len(str(abs(n)))  # Count digits ignoring the sign
    return n * (5 ** num_digits)
