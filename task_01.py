marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
def is_palindrome(str_input):
    for i in marks:
        if i in str_input:
            str_input = str_input.replace(i, '')
    if str_input.upper() == str_input[::-1].upper():
        print(True)
    else:
        print(False)
str_input=input('Введите строку, которую вы хотите проверить:')
is_palindrome(str_input)
