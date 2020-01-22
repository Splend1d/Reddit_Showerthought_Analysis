'''*************************************************************************
    FileName        [ parseTFTF.py ]
    Synopsis        [ calculate TFTF ]
    Author          [ Chan-Jan(Jeff) Hsu ]
    Copyright       [ Copyleft(c) 2020]
****************************************************************************
    Input           ./attrs/corpus_words.json : target corpus (with only title) (r/showerthoughts)
    				../Reddit_Data/attrs/corpus_words.json : corpus with only title (all reddit)
    				corpus_words_common_200 : most common word in target corpus
    Output          tftf.json : corpus term frequency importance
    Dependencies    parsewordsALL.py, parsewords.py and its dependencies
*************************************************************************'''
import json
total_words = 0
with open("../Reddit_Data/raw/attrs/corpus_words.json","r") as fread:
    corpus = json.load(fread)

all_corpus = {}
for k,v in corpus.items():
	try:
		all_corpus[k.lower()] += v
	except:
		all_corpus[k.lower()] = v
	total_words += v
	#print(k,corpus[k])

print("total words in reddit: ", total_words)



with open("./attrs/corpus_words.json","r") as fread:
    corpus = json.load(fread)

target_total_words = 0
for k,v in corpus['all'].items():
	target_total_words += v

with open("./attrs/corpus_words_common_200.json","r") as fread:
    corpus = json.load(fread)

target_corpus = {}
for k,v in corpus['all'].items():
	try:
		target_corpus[k.lower()] += v
	except:
		target_corpus[k.lower()] = v
	#target_total_words += v
	#print(k,corpus[k])

print("total words in showerthoughts: ", target_total_words)
for k,v in target_corpus.items():
	target_corpus[k] /= target_total_words
	if k not in all_corpus:
		target_corpus[k] = 0
		print("error:",k)
	else:
		target_corpus[k] /= all_corpus[k]
		target_corpus[k] *= total_words
tftf = {k: v for k, v in sorted(target_corpus.items(), key=lambda item: item[1], reverse = True)}
print(tftf)
with open("./attrs/tftf.json","w") as f:
    json.dump(tftf,f)