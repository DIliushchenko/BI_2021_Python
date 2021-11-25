import re
import matplotlib.pyplot as plt
import seaborn as sns
pattern = re.compile('^ftp')

with open('references.txt', 'r') as ref:
    with open('ftps.txt', 'w') as answ:
        for line in ref:
            line = line.replace(';', ' ')
            line = line.rsplit()
            for obj in line:
                if pattern.search(obj):
                    answ.write(obj + '\n')

num_all_in_text = []
word_with_a = []
pattern_num = re.compile('[0-9]+')
pattern_a_word = re.compile('[Aa]')
with open('2430AD.txt', 'r') as good_book:
    for line in good_book:
        line = line.replace(',', ' ')  # delete situation, when 1969,"
        line = line.rsplit()
        for obj in line:
            # check if num in element of text
            if pattern_num.search(obj):
                num_all_in_text.append(obj)
            # check if word with 'a' or 'A' in word
            elif pattern_a_word.search(obj):
                word_with_a.append(obj)

print(num_all_in_text)
print(word_with_a)


word_pattern = re.compile(r'.*\w+\b')
un_word_list = []
with open('2430AD.txt', 'r') as good_book:
    for line in good_book:
        line = line.rsplit()
        for obj in line:
            if not pattern_num.search(obj) and (obj not in un_word_list):
                un_word_list.append(obj)

len_word = [0] * len(un_word_list)

for i in range(len(un_word_list)):
    len_word[i] += len(un_word_list[i])

b_l = list(range(1, max(len_word)))
plt.hist(len_word, align='left', bins=b_l, color='#44b086', density=True)
plt.xlabel('Length of word')
plt.title('Distribution of words lengths')
plt.show()
