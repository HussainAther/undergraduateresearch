import fileinput 
import random
l=[ ]
f=open("/Users/Mcfoofa/Google Drive/Research/My Research/Drosophila/chromosomes/dsim_2L_new.fasta", "r")
for i in f:
	if i not startswith.(">"):
		for j in range(1000):
			e=random.randit(0,len(i)-1001)
			l.append(e)
print l
	