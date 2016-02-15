#q5_count_letter.py
def count_letter(string, ch):
    if not string: #terminating condition of empty string
        return 0
    return (1 if ch==string[0] else 0) + count_letter(string[1:],ch)
