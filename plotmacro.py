'''*************************************************************************
  FileName     [ plotcommon.py ]
  Synopsis     [ plot graph of macro attributes ]
  Author       [ Chan-Jan(Jeff) Hsu ]
  Copyright    [ Copyleft(c) 2020]
****************************************************************************
  Input		   macro_*.json : staticstic of all or partial target corpus 
  Output	   word_distribution.png : x - length of entry, y - number of entries
  			   upvote_distribution.png : x - number of upvotes (log), y - number of entries
  Dependencies run genmacro.py first, and genliked.py(optional)
*************************************************************************'''
import matplotlib.pyplot as plt
import json
_name = ["","_ups","_awards"]
for n in _name:

	with open("./attrs/macro"+n+".json","r") as f:
		macro = json.load(f)
	#print(macro)
	if "distribution_title_length" in macro:
		xs = []
		ys = []
		for i in range(100):
			xs.append(i)
			ys.append(macro["distribution_title_length"][str(i)])
		plt.bar(xs,ys, color = "blue")
		plt.savefig('./attrs/length_distribution'+n+'.png', bbox_inches='tight')
		plt.show()
	if "distribution_upvotes" in macro:
		xs = []
		ys = []
		for i in range(20):
			xs.append(i)
			ys.append(macro["distribution_upvotes"][str(i)])

		plt.bar(xs,ys, color = "blue")
		plt.savefig('./attrs/upvote_distribution'+n+'.png', bbox_inches='tight')
		plt.show()
