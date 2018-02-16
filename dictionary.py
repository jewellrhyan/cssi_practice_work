dictionary = {"bts": {"s/p" : "s",
                             "p_s" : "n",
                             "meaning" : "my life",
                             "translation": {"Korean" : "bangtan sonyeondan",
                                             "english" : "beyond the scene",
                                             "french" : "BTS"}}}

print dictionary['bts']['translation']['french']

#def shouted_word(word):


def shout_korean(word):
    if word in dictionary:
        word_dictionary = dictionary[word]
        if 'translation' in word_dictionary:
            all_translation = word_dictionary['translation']
            if 'Korean' in all_translation:
                translation_word = all_translation['Korean']
#                shouted_word = shouted_word[translation_word]
#                return shouted_word
#    print None
