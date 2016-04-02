import codecs
fo = codecs.open("tags.txt","a")
i =1 
while(i<=50):

	if i<=25:
		fo.write("1"+"\n")
	else:
		fo.write("0"+"\n")
	i+=1
fo.close()
