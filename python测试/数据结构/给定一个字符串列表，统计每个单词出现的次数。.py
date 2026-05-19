words = ["apple", "banana", "apple", "orange", "banana", "apple"]
dict_words = {}
for word in words:
    dict_words[word] = dict_words.get(word, 0) + 1

print(dict_words)