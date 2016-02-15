#q6_sum_digits(n)
def sum_digits(n):
    if n==0:
        return 0
    else:
        return n%10+int(sum_digits(n//10))
