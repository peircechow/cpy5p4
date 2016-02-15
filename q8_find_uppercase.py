#q8_find_uppercase.py

def find_num_uppercase(a):
    if not a:
        return 0
    else:
        if a[0]!=a[0].upper():
            return find_num_uppercase(a[1:])
        else:
            return 1+find_num_uppercase(a[1:])
