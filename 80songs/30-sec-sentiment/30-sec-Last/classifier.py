
import matlab.engine
eng = matlab.engine.start_matlab()
eng.svmout(nargout=0)
eng.naiveout(nargout=0)
import os
import itertools
try:
	os.remove("comparision.txt")
except OSError:
	pass

testTags,svmTags,naiveTags,songIDs=[],[],[],[]
with open("testTags.txt","r") as f1, open("svm-output.txt","r") as f2, open("naive-output.txt","r") as f3,open("testSongIDs.txt","r")as f4,open("comparision.txt","a")as f5:
		for line in f1:
			testTags.append(line.strip())
		for line in f2:
			svmTags.append(line.strip())
		for line in f3:
			naiveTags.append(line.strip())
		for line in f4:
			songIDs.append(line.strip())

		for tt,st,nt,s_id in itertools.izip(testTags,svmTags,naiveTags,songIDs):
			f5.write("songID = "+str(s_id)+" OriginalTag = "+str(tt)+" svmTag = "+str(st)+" naiveTag = "+str(nt)+"\n")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
print "file comparision.txt generated "
			
