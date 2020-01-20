'''*************************************************************************
  FileName     [ plotcommon.py ]
  Synopsis     [ plot graph of distribution of most common words ]
  Author       [ Chan-Jan(Jeff) Hsu ]
  Copyright    [ Copyleft(c) 2020]
****************************************************************************
  Input		   corpus_words_common_(int).json : staticstic of (int) most common corpus words 
  Output	   common.png : x - normalized ith most common word, y - frequency of ith most common word 
  Dependencies run parsewords.py first
*************************************************************************'''
import json
import matplotlib.pyplot as plt
import numpy as np

with open("./attrs/corpus_words_common_200.json","r") as f:
	db = json.load(f)

print(db['all'].keys())
print(db['start'].keys())
print(db['end'].keys())
ys = {}
for k in db.keys():
	xs = []
	ys[k] = []
	all_keys = list(db[k].keys())
	for i in range(1,21):
		xs.append(i)
		ys[k].append(db[k][all_keys[i]])

plt.figure(figsize=(20,10))
type_ = ['all','start','end']
#ax = plt.subplot(111)
plt.bar([x-0.2 for x in xs], [y/18.52 for y in ys['all']], width=0.2, color='green', align='center')
plt.bar(xs, ys['start'], width=0.2, color='b', align='center')
plt.bar([x+0.2 for x in xs], ys['end'], width=0.2, color='orange', align='center')
plt.legend(type_,loc="upper right")	
plt.xticks(np.arange(1, 21, step=1))
plt.title("n-th most popular word - normalized counts")
plt.savefig('./attrs/common.png', bbox_inches='tight')
plt.show()