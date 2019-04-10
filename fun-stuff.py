import re
import random

with open('moby-dick.txt','r') as moby:
    lines = moby.read()

words = []
chain = {}
punctuation = ['.','?','!']
character = []
par_reg = r"\(.*\)"


#take out line breaks and append to list
lines = lines.replace('\r',' ').replace('\n',' ')
lines = re.sub(par_reg, '', lines)

new_words = lines.split(' ')
words = words + new_words
#takes out empty strings
words = [i for i in words if i]


for word in words:
    if word[len(word)-1] == ':':
        character.append(word)

corp_len = len(words)
for i,key1 in enumerate(words):
    if corp_len > (i+2):
        key2 = words[i+1]
        word = words[i+2]
        if (key1, key2) not in chain:
            chain[(key1,key2)] = [word]
        else:
            chain[(key1,key2)].append(word)

moby_sent = random.choice(words)
ran_int = random.randrange(0, len(words)-1)
moby_key = (words[ran_int],words[ran_int + 1])
moby_word = moby_sent + moby_key[0] + ' ' + moby_key[1]

while len(moby_sent) < 100:
    moby_word2 = random.choice(chain[moby_key])
    moby_sent += ' ' + moby_word2
    moby_key = (moby_key[1], moby_word2)

if moby_sent[-1] not in punctuation:
    ran_int = random.randrange(0, len(punctuation)-1)
    moby_sent += punctuation[ran_int]

print(moby_sent)
