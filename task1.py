def split_numbers(str):
    digit,nodigit,f, num = [],"", False, 0
    for i in str:
        if not i.isdigit():
            if f:
                f = False
                digit.append(num)
                num = 0
            nodigit += i
        else:
            f = True
            num*=10
            num+=int(i)
    if f:
        digit.append(num)
    return digit, nodigit
    
def capitalize(str):
    str, result = str.title(), ""
    for word in str.split():
        result += word[:-1] + word[-1].upper() + " "
    return result


str = input("Input string: ")

numbers, words = split_numbers(str)
print(numbers)
print(words)
    
words = capitalize(words);

max_num = max(numbers)
numbers_pow = numbers
numbers_pow.remove(max_num)
numbers_pow = [x ** i for i, x in enumerate(numbers_pow)]