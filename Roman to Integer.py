s = 'IV'
s = 'V'
s = 'III'
s = 'LXXXIV'
s = 'LVIII'
s = 'MCMXCIV'
s = 'MMMCMXCIX'
s = 'MCMXCVI'
s = 'MCMXCVII'
# s = 'MM'

def Roman_to_Int(s: str):

    match = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = 0
    result = []
    for n in s:
        digit = match[s[i]]
        if i == len(s)-1:
            result.append(digit)
            break
        else:
            nxt_digit = match[s[i + 1]]
            if nxt_digit > digit:
                result.append(nxt_digit - digit)
                if i+2 <= len(s)-1:
                    i += 2
                else:
                    break
            else:
                result.append(digit)
                i += 1

    return sum(result)


print(Roman_to_Int(s))