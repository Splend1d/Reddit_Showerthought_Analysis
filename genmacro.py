import json
import datetime
import sys
import os
import nltk
from nltk.tokenize import word_tokenize as tokenize

files = [f for f in os.listdir('data') if "TRS" in f]
print("targets:",files)
scores = []
total_score = 0
total_entries = 0
total_words = 0
distribution_words = {}
for i in range(250):
	distribution_words[i] = 0
distribution_upvotes = {}
for i in range(20):
	distribution_upvotes[i] = 0
corpus = []
corpus_w_info = []

for fname in files:
	min_time = sys.maxsize
	max_time = 0 
	print("analyzing",fname)
	with open('./data/'+fname,'r') as json_file:
		data = json.load(json_file)
	for entry in data:
		#----IMPORTANT----
		try:
			gildings = entry['gildings'] # dict: type of badges and amount
		except:
			gildings = {}
		
		try:
			total_awards_received = entry['total_awards_received']
		except:
			pass
		created_utc = entry['created_utc']
		num_comments = entry['num_comments']
		score = entry['score']
		title = entry['title'] # string : title IS the corpus
		gilded = entry['gilded'] # int: number of badges
		
		#----IMPORTANT----
		#scores.append(score)
		total_score += score
		for i in range(20):
			if 2**(i-1)<score and score<2 ** i:
				distribution_upvotes[i] += 1; 
		total_entries += 1
		tokens = tokenize(title)
		total_words += len(tokens)
		distribution_words[len(tokens)] += 1
		corpus.append(tokens)
		corpus_w_info.append({})
		corpus_w_info[-1]['entry'] = tokens
		corpus_w_info[-1]['time'] = created_utc
		corpus_w_info[-1]['score'] = score
		corpus_w_info[-1]['awards'] = gildings
		corpus_w_info[-1]['n_comments'] = num_comments
		


print("total_words")
print(total_words) # words in corpus
print("total_entries")
print(total_entries) # sentence in corpus
print("distribution_words")
print(distribution_words)# distribution of words
print("avg_words")
print(total_words/total_entries) # avg words
print("avg_upvotes")
print(total_score/total_entries) # avg upvotes
print("distribution_upvotes")
print(distribution_upvotes) # distribution of upvotes
macro = {}
macro["total_words"] = total_words
macro["total_entries"] = total_entries
macro["distribution_title_length"] = distribution_words
macro["avg_title_length"] = total_words/total_entries
macro["avg_upvotes"] = total_score/total_entries
macro["distribution_upvotes"] = distribution_upvotes

with open("./attrs/macro.json","w") as f:
	json.dump(macro,f)

with open("./data/corpus_w_info.json","w") as f:
	json.dump(corpus_w_info,f)

with open("./data/corpus.json","w") as f:
	json.dump(corpus,f)
