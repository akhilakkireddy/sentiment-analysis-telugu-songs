import os
import codecs
import random
import itertools
fo1= open("trainedVectors.txt","r")
fo2= open("tags.txt","r")
fo3= codecs.open("data.txt","r")
vectors,tags,songs = [],[],[]

for line in fo1:
	vectors.append(line.strip())
for line in fo2:
	tags.append(line.strip())
for line in fo3:
	songs.append(line.strip())
song_ids = range(1,len(tags)+1)
combined = zip(vectors,tags,songs,song_ids)
random.shuffle(combined)
#random.shuffle(combined)
vectors[:],tags[:],songs[:],song_ids[:] = zip(*combined)
fo1.close()
fo2.close()
fo3.close()
try:
        os.remove("trainData.txt")
except OSError:
        pass
try:
        os.remove("trainTags.txt")
except OSError:
        pass
try:
        os.remove("testData.txt")
except OSError:
        pass
try:
        os.remove("testTags.txt")
except OSError:
        pass
try:
		os.remove("testSongIDs.txt")
except OSError:
		pass
oc,zc = 0,0
with open("trainData.txt","a") as f1, open("trainTags.txt","a") as f2, open("testData.txt","a") as f3, open("testTags.txt","a") as f4, open("testSongIDs.txt","a") as f5:
	for v,t,s_id in itertools.izip(vectors,tags,song_ids):
		'''
		if t=="1":
			oc+=1
			if oc<=5:
				f3.write(v+"\n")
				f4.write(t+"\n")
				f5.write(str(s_id)+"\n")

			else:
				f1.write(v+"\n")
				f2.write(t+"\n")
		else:
			zc+=1
			if zc<=5:
				f3.write(v+"\n")
				f4.write(t+"\n")
				f5.write(str(s_id)+"\n")
			else:
				f1.write(v+"\n")
				f2.write(t+"\n")
		'''
		if s_id in [21,22,23,24,25,46,47,48,49,50]:
			f3.write(v+"\n")
			f4.write(t+"\n")
			f5.write(str(s_id)+"\n")
		else:
			f1.write(v+"\n")
			f2.write(t+"\n")
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
