'''*************************************************************************
    FileName        [ parsewordsALL.py ]
    Synopsis        [ perform word related parsing to ALL ]
    Author          [ Chan-Jan(Jeff) Hsu ]
    Copyright       [ Copyleft(c) 2020]
****************************************************************************
    Input           corpus_title.json : corpus with only title (all reddit)
    Output          corpus_words.json : corpus word distribution (all reddit)
    Dependencies    parseALL.py, genmacro.py
*************************************************************************'''
import os
import json
files = [f for f in os.listdir("../Reddit_Data/raw/") if "corpus_title_" in f]
print(files)
wordcountALL = {}
for f in files:
    print("parsing:",f)
    with open("../Reddit_Data/raw/"+f,"r") as fread:
        corpus = json.load(fread)
        for l in corpus:
            for w in l:
                if w.isalpha():
                    try:
                        wordcountALL[w] += 1
                    except:
                        wordcountALL[w] = 1
    print("finish parsing:",f)

wordcountALL = {k: v for k, v in sorted(wordcountALL.items(), key=lambda item: item[1], reverse = True)}
with open("../Reddit_Data/raw/attrs/corpus_words.json","w") as f:
    json.dump(wordcountALL,f)
        