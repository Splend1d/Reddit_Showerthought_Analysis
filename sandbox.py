import json

with open("./attrs/corpus_words_common_200.json","r") as f:
	db = json.load(f)

print(db['all'].keys())