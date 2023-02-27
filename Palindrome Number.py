x = 1000001

def Palindrome_number(x):
    n = str(x)
    index_first = 0
    index_last = len(n)-1
    result = False
    for digit in n:
        if n[index_first] == n[index_last]:
            result = True
            index_first += 1
            index_last -= 1
        else:
            result = False
            break
    return result


print(Palindrome_number(x))