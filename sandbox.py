from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict

tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

text = "Another way of achieving this task. I ate an apple."
text2 = "ate"
tokens = word_tokenize(text)
lmtzr = WordNetLemmatizer()

for token, tag in pos_tag(tokens):
    lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
    print(token, "=>", lemma, tag)
lemma2 = lmtzr.lemmatize(text2,tag_map['0'])
print(lemma2)