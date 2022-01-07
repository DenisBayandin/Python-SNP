marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
def is_palindrome(string):
    string = str(string)
    for i in marks:
        if i in string:
            string = string.replace(i, '')
    if string.upper() == string[::-1].upper():
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
