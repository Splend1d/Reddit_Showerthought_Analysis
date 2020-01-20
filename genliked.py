'''*************************************************************************
  FileName     [ genliked.py ]
  Synopsis     [ Generate macro analysis files from raw file that are praised ]
  Author       [ Chan-Jan(Jeff) Hsu ]
  Copyright    [ Copyleft(c) 2020]
****************************************************************************
  Input		   corpus_w_info.json : target raw corpus (r/showerthoughts)
  Output	   macro_ups.json : statistic info of raw corpus that are praised
  			   macro_awards.json : statistic info of raw corpus that have awards
  			   corpus_ups.json : target corpus that are praised with only words 
  			   corpus_downs.json : target corpus that are not praised with only words
  			   corpus_awards.json : target corpus that are awarded with only words
  Dependencies run genmacro.py first
*************************************************************************'''
import json
from nltk.tokenize import word_tokenize as tokenize
from nltk.corpus import stopwords
_stop_words = set(stopwords.words('english'))

upentries = []
downentries = []
awardentries = []
awardscore = {}
for i in range(20):
	awardscore[i] = 0

total_score = [0,0]
average_score = [0,0]
total_words = [0,0]
average_words = [0,0]
distribution_words = [{},{}]
for i in range(250):
	distribution_words[0][i] = 0
	distribution_words[1][i] = 0

with open("./data/corpus_w_info.json","r") as f:
	entries = json.load(f)

for e in entries:
	#print(e)
	time = e['time']
	n_comments = e['n_comments']
	score = e['score']
	entry = e['entry'] # string : title IS the corpus
	awards = e['awards'] # int: number of badges
	#if len(e["awards"]) != 0:
	for v in e["awards"].values():
		if v != 0:
			awardentries.append(entry)
			for i in range(20):
				if 2**(i-1)<score and score<2 ** i:
					awardscore[i] += 1; 
			total_score[1] += score
			total_words[1] += len(entry)
			distribution_words[1][len(entry)] += 1

			break

	if score >= 64:
		upentries.append(entry)
		total_score[0] += score
		total_words[0] += len(entry)
		distribution_words[0][len(entry)] += 1
	elif score < 64:
		downentries.append(entry)

with open("./data/corpus_ups.json","w") as f:
	json.dump(upentries,f)
with open("./data/corpus_downs.json","w") as f:
	json.dump(downentries,f)
with open("./data/corpus_awards.json","w") as f:
	json.dump(awardentries,f)

print("total_words")
print(total_words) # words in corpus
print("total_entries")
print([len(upentries),len(awardentries)]) # sentence in corpus
print("distribution_words")
print(distribution_words)# distribution of words
print("avg_words")
print([total_words[0]/len(upentries), total_words[1]/len(awardentries)]) # avg words
print("avg_upvotes")
print([total_score[0]/len(upentries), total_score[1]/len(awardentries)]) # avg upvotes
print("distribution_upvotes")
print(awardscore) # distribution of upvotes
macro = [{},{}]
for i in range(2):
	macro[i]["total_words"] = total_words[i]
	macro[i]["distribution_title_length"] = distribution_words[i]

macro[1]["distribution_upvotes"] = awardscore
macro[0]["total_entries"]= len(upentries)
macro[1]["total_entries"] = len(awardentries)
macro[0]["avg_words"] = total_words[0]/len(upentries)
macro[1]["avg_words"] = total_words[1]/len(awardentries)
macro[0]["avg_score"] = total_score[0]/len(upentries)
macro[1]["avg_score"] = total_score[1]/len(awardentries)
with open("./attrs/macro_ups.json","w") as f:
	json.dump(macro[0],f)
with open("./attrs/macro_awards.json","w") as f:
	json.dump(macro[1],f)