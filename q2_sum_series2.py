#q2_sum_series2.py
def sum_series2(i):
    if i==1:
        return 1/3
    else:
        return 1/(i+i+1)+sum_series2(i-1)
