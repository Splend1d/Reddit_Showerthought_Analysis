import json
import os 
to_do_files = [f for f in os.listdir('./raw') if os.path.isfile(f) and "RS" in f and "TRS" not in f]
done_files = [f for f in os.listdir('./raw') if os.path.isfile(f) and "TRS" in f]
print(to_do_files)
print(done_files)
n_target_total = 0
for fname in to_do_files:
	if "T" + fname +".json" in done_files:
		print(fname, "done")
		continue
	print("parsing ", fname)
	# one month of data
	# fname = (year)-(month)
	n_target_month = 0
	n_data_month = 0
	target_corpus_month = []
	with open(fname, "r") as file:
		for entry in file:
			entry_dict = json.loads(entry)
			try:
				if entry_dict["subreddit"] == "Showerthoughts":
					#print(json.dumps(entry_dict, indent=4, sort_keys=True)
					target_corpus_month.append(entry_dict)
					n_target_month += 1;
			except:
				continue # ads DansGame
			n_data_month += 1;
			#if n_data_month % 100000 == 0:
				#print(n_data_month, "entries done,", n_target_month,"showerthoughts entries")
	#print(n_data_month, "entries done,", n_target_month,"showerthoughts entries in",fname)
	n_target_total += n_target_month
	with open('T'+fname+'.json', 'w') as outfile:
		json.dump(target_corpus_month, outfile)
	with open('stats.txt', 'a') as outfile:
		outfile.write(",".join([fname,str(n_target_month),str(n_data_month)])+'\n')
