'''*************************************************************************
  FileName     [ parsewords.py ]
  Synopsis     [ Generate macro analysis files from raw file ]
  Author       [ Chan-Jan(Jeff) Hsu ]
  Copyright    [ Copyleft(c) 2020]
****************************************************************************
  Input		   corpus.json : target corpus with only words 
  Output	   corpus_words.json : staticstic of corpus words.
  			   corpus_words_common_(int).json : staticstic of (int) most common corpus words
  Dependencies run genmacro.py first
*************************************************************************'''
import os
import json
from nltk.corpus import stopwords
_stop_words = set(stopwords.words('english'))

class word_parser:
	def __init__(self,db):
		
		self.db = db

		self.corpus_words = {}
		self.corpus_sentence_start = {}
		self.corpus_sentence_end = {}

		self.swapdict = {}
		self.swaplist = []

	def save(self,p):
		print("saving", p)
		if p == "freq":
			with open("./attrs/corpus_words.json","w") as f:
				json.dump({"all":self.corpus_words,"start":self.corpus_sentence_start,"end":self.corpus_sentence_end},f)
		elif p == "common":
			with open("./attrs/corpus_words_common_"+str(len(self.corpus_words))+".json","w") as f:
				json.dump({"all":self.corpus_words,"start":self.corpus_sentence_start,"end":self.corpus_sentence_end},f)

	def get_freq(self):
		print("getting freq")
		for entry in self.db:
			for word in entry:
				if word.isalpha():
					try:
						self.corpus_words[word.lower()] += 1
					except:
						self.corpus_words[word.lower()] = 1
			for i in range(len(entry)):
				if entry[i].isalpha():
					try:
						self.corpus_sentence_start[entry[i].lower()] += 1
					except:
						self.corpus_sentence_start[entry[i].lower()] = 1
					finally:
						break

			for i in range(len(entry)-1,-1,-1):
				if entry[i].isalpha():
					try:
						self.corpus_sentence_end[entry[i].lower()] += 1
					except:
						self.corpus_sentence_end[entry[i].lower()] = 1
					finally:
						break
		self.corpus_words = {k: v for k, v in sorted(self.corpus_words.items(), key=lambda item: item[1], reverse = True)}
		self.corpus_sentence_start = {k: v for k, v in sorted(self.corpus_sentence_start.items(), key=lambda item: item[1], reverse = True)}
		self.corpus_sentence_end = {k: v for k, v in sorted(self.corpus_sentence_end.items(), key=lambda item: item[1], reverse = True)}

	
	def get_common(self, length):
		'''
		func : gets top frequency of stop words
		reads list of (word, freq)
		returns list of (word, freq)
		'''
		swaplist = [[k,v] for k,v in self.corpus_words.items()][:length]
		self.corpus_words = {k:v for [k,v] in swaplist}
		#print(self.corpus_words)
		swaplist = [[k,v] for k,v in self.corpus_sentence_start.items()][:length]
		self.corpus_sentence_start = {k:v for [k,v] in swaplist}
		#print(self.corpus_sentence_start)
		swaplist = [[k,v] for k,v in self.corpus_sentence_end.items()][:length]
		self.corpus_sentence_end = {k:v for [k,v] in swaplist}
		#print(self.corpus_sentence_end)

	def rm_stopwords(self):
		'''
		func : removes stopwords
		reads list of (word, freq)
		returns list of (word, freq)
		'''
		self.corpus_words = {k: v for k, v in self.corpus_words.items() if k not in _stop_words}
		self.corpus_sentence_start = {k: v for k,v in self.corpus_sentence_start.items() if k not in _stop_words}
		self.corpus_sentence_end = {k: v for k, v in self.corpus_sentence_end.items() if k not in _stop_words}
		
_name = "corpus"
_redo = True
with open("./data/corpus.json","r") as f:
	corpus = json.load(f)
p = word_parser(corpus)
if "corpus_words.json" not in os.listdir("attrs") or _redo:
	p.get_freq()
	p.save("freq")
else:
	with open("./attrs/corpus_words.json","r") as f:
		data = json.load(f)
	p.corpus_words = data['all']
	p.corpus_sentence_start = data['start']
	p.corpus_sentence_end = data['end']
p.rm_stopwords()
p.get_common(200)
p.save("common")

