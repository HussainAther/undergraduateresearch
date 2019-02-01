file=open("/Users/Mcfoofa/Desktop/databases/dmel-3L-chromosome-r5.55.fasta", "r")
a=[]
c=""
d=""
for line in file:
	if line[0]!=">":
		c += line.replace("\n", "")
# 	if line.startswith(">"):
# 		a.append(c)
# 		c=""
print c
# a.append(c)
# a.pop(0)
# for i in a:
# 	print i