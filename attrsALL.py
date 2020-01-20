import json
import datetime
import sys
import os
import nltk
from nltk.tokenize import word_tokenize as tokenize

files = [f for f in os.listdir('../Reddit_Data/raw') if "RS" in f and "TRS" not in f and f >= "RS_2019-04"]
print("targets:",files)
scores = []
corpus_t = []
corpus_b = []
distribution_words = {}
for i in range(250):
	distribution_words[i] = 0
total_entries = 0
total_words_t = 0
total_words_b = 0
for n,fname in enumerate(files):
	min_time = sys.maxsize
	max_time = 0 
	print("analyzing",fname)
	with open('../Reddit_Data/raw/'+fname,'r') as f:
		for entry in f:
			entry = json.loads(entry)
			if 'subreddit' not in entry:
				continue
			#count += 1
			if 'title' in entry:
				title = entry["title"]
				tokens = tokenize(title)
				corpus_t.append(tokens)
				total_words_t += len(tokens)
				try:
					distribution_words[len(tokens)] += 1
				except:
					distribution_words[249] += 1


			if 'selftext' in entry:
				selftext = entry["selftext"]
				tokens = tokenize(selftext)
				if len(tokens) != 0:
					corpus_b.append(tokens)
				total_words_b += len(tokens)
			total_entries += 1
			
			#distribution_words[len(tokens)] += 1
	with open("../Reddit_Data/raw/corpus_title_"+str(n)+".json","w") as f:
		json.dump(corpus_t,f)
	corpus_t = []
	with open("../Reddit_Data/raw/corpus_body_"+str(n)+".json","w") as f:
		json.dump(corpus_b,f)
	corpus_b = []	

	print("finished analyzing",fname)

print("total_words in title")
print(total_words_t) # words in corpus title 
print("total_words in body")
print(total_words_b) # words in corpus body
print("total_entries")
print(total_entries) 
print("avg_title_length")
print(total_words_t/total_entries) # avg words
macro = {}
macro["total_words_t"] = total_words_t
macro["total_words_t"] = total_words_b
macro["total_entries"] = total_entries
macro["avg_title_length"] = total_words_t/total_entries
macro["distribution_title_length"] = distribution_words
with open("../Reddit_Data/raw/attrs/macro.json","w") as f:
	json.dump(macro,f)


