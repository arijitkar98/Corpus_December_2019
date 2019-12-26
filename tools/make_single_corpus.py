from os import listdir
from os.path import isfile, join

files = [f for f in listdir("../raw_corpus/separate_files/") if isfile(join("../raw_corpus/separate_files/", f))]
print(files)

with open("../raw_corpus/raw.txt",'w') as f:
	for file in files:
		with open(join("../raw_corpus/separate_files/", file)) as f1:
			for line in f1:
				f.write(line)

