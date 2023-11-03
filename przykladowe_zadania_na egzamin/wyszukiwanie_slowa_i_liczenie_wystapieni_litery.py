def find_short_words(word_list):
    short_words = [word for word in word_list if len(word) < 5]
    return short_words

word_list = ['Litwo', 'ojczyzno', 'moja', 'ty', 'jestes', 'jak', 'zdrowie']
short_word_list = find_short_words(word_list)
print(short_word_list)

def count_letter_a(sentence):
    count = 0
    for letter in sentence:
        if letter.lower() == 'a':
            count += 1
    return count

sentence = "Ala ma kota"
letter_count = count_letter_a(sentence)
print(letter_count)