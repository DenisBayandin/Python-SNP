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


is_palindrome("A man, a plan, a canal -- Panama")  # --> True
is_palindrome("Madam, I'm Adam!")  # --> True
is_palindrome(333)  # --> True
is_palindrome(None)  # --> False
is_palindrome("Abracadabra")  # --> False
