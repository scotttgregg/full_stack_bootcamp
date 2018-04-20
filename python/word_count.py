# word_count.py

# import string
import string
# import operator
import operator

# opens oscar_wilde.txt - reading - encoding
with open('oscar_wilde.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

clean_text = ''

for i in text:
    if i in string.ascii_letters + ' ':
        clean_text += i
    else:
        clean_text += ' '

word_list = clean_text.split()

word_dict = {}

for i in word_list:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

sorted_list = sorted(
                    list(word_dict.items()),
                    key=operator.itemgetter(1), reverse=False)
print(sorted_list[-10:])
