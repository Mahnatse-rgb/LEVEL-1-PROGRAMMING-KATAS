def longest_word(word_list):
    lw = []
    longest = word_list[0]
    lw.append(longest)
    for i in range(1, len(word_list)):
        if len(word_list[i]) > len(longest):
            longest = word_list[i]
            lw.clear()
            lw.append(longest)
        elif len(word_list[i]) == len(longest):
            lw.append(word_list[i])
        else:
            continue
    return lw
# Testing our function
mylist = ['the', 'quick', 'brown', 'fox', 'ate', 'my', 'chickens']
longest_words = longest_word(mylist)
for i in range(len(longest_words)):
    print(longest_words[i])