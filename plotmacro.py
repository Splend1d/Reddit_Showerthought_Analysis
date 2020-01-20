import matplotlib.pyplot as plt
import json
_name = "_awards"
with open("./attrs/macro"+_name+".json","r") as f:
	macro = json.load(f)
print(macro)
xs = []
ys = []
for i in range(100):
	xs.append(i)
	ys.append(macro["distribution_title_length"][str(i)])
plt.bar(xs,ys, color = "blue")
plt.savefig('./attrs/word_distribution'+_name+'.png', bbox_inches='tight')
plt.show()
xs = []
ys = []
for i in range(20):
	xs.append(i)
	ys.append(macro["distribution_upvotes"][str(i)])

plt.bar(xs,ys, color = "blue")
plt.savefig('./attrs/common'+_name+'.png', bbox_inches='tight')
plt.show()
