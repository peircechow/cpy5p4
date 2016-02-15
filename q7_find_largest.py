# q7_find_largest.py
def find_largest(a):
    if len(a)==1:
        return a[0]
    else:
        if a[-1]>=a[-2]:
            del a[-2]
        else:
            del a[-1]
        return find_largest(a)

