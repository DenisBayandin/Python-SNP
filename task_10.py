def count_words(string):
    count_word = {}
    marks = '-,'
    for i in marks:
        if i in string:
            string = string.replace(i, '')
    new_string = string.lower().split()
    for word in new_string:
        digit = new_string.count(word)
        count_word[word] = digit
    return count_word
count_words("A man, a plan, a canal -- Panama") # --> {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
count_words("Doo bee doo bee doo")  # --> {'doo': 3, 'bee': 2}