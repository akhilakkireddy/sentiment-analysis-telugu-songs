import os
from shuffle import songs
try:
	os.remove("validate.txt")
except OSError:
	pass
fo1 = open("matlab-output.txt","r")
fo2 = open("validate.txt","a")
songs=songs[25:]
i = 0
for line in fo1:
	fo2.write(songs[i]+"\n")
	i += 1
	fo2.write(line+"\n")

fo1.close()
fo2.close()


