
import os
import codecs
try:
	os.remove("sadOutput")
except OSError:
	pass
f2 = codecs.open("sadOutput","a","utf-8")
for fi in os.listdir("./"):
	if fi.endswith(".txt"):
		f1 = codecs.open(fi,"r","utf-8")
		content = f1.read()
		content=" ".join(content.splitlines())	
		f2.write(content+u"\n")
f2.close()
		
