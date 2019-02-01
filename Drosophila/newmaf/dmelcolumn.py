from __future__ import division
# Change this so that it works on the Linux computer at IU and run it from there
# Now write something that finds the d string in c string with a certain percent accuracy by checking chunks of c string of size d string
# f=open("/Users/Mcfoofa/Google Drive/Research/My Research/Drosophila/newmaf/dmel/2Lref/2L_columns.txt", "r")
# g=open("/Users/Mcfoofa/Google Drive/Research/My Research/Drosophila/newmaf/2Lsampleduplication.txt", "r")
# f=open("/home/hussainather/progressiveCactus/2L_columns.txt", "r")
# g=open("/home/hussainather/progressiveCactus/2Lsampleduplication.txt", "r")
f=open("/Users/Mcfoofa/Desktop/databases/dmel3LwithRdl.txt", "r")
g=open("/Users/Mcfoofa/Desktop/databases/Rdlgene.txt", "r")
c=[] # our reference string
d="" # the string we're looking for
for i in g.readlines():
	if not i.startswith(">"):
		d+=i.replace("\n", "").lower()
# for i in f.readlines():
# 	if i.split(" ")[0]!="N":
# 		c.append(i.split(" ")[0].lower())
for i in f.readlines():
	for j in i:
		c.append(j.replace("\n", "").lower())
# print c
# print d
l=len(c)
h=len(d)
print l
print h
# print str(c) + str(l)
# print str(d) + str(h)
# for j in range(l-h):
# 	if c[j]!="N" and c[j]!="-":
# 		p=0
# 		for o in range(h):
# 			if c[j+o]==d[o]:
# 				p+=1
# 			if p==h-400:
# 				print j
for j in range(l-h): # this one will split the window into subwindows
# 	print "searching winwdows..." + str(j) + "out of" + str(l)
	if c[j]!="N" and c[j]!="-":
		p=0
		pt=0
		n=600 # size of subwindow
		for y in range(60): # put the number of subwindows in here
			w=n*y
			for u in range(len(c[j+w:j+n+w])):
				p=0
				for o in range(u):
					if c[j+o]==d[o]:
						p+=1
					if p==500:# put this as the number of successful bases per subwindow to define a successful subwindow  (probably n-100)
						pt+=1
		if pt==50: #put this as the threshold number of successful subwindows to find a match
			print "match" + str(j)