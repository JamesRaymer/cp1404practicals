text_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    counter = text_to_count.get(word, 0)
    if counter == 0:
        text_to_count[word] = 1
    else:
        text_to_count[word] = counter + 1
word_list = list(text_to_count.keys())
word_list.sort()
for string in word_list:
    longest_word = len(max(string))
    print("{:{}} : {}".format(string, longest_word, text_to_count[string]))
