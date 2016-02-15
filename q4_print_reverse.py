#q4_print_reverse.py
def reverse_int(n):
    if n==0:
        return ''
    else:
        return str(n%10)+ str(reverse_int(n//10))
