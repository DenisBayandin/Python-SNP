from collections import Counter, defaultdict

def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        an = tuple(Counter(word).items())
        anagrams[tuple(sorted(an))].append(word)
    return list(anagrams.values())

words = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
anagram(words)  # --> [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]