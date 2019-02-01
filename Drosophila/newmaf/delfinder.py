# prints the length of each duplication from the del.bed file
f=open("/Users/Mcfoofa/Google Drive/Research/My Research/Drosophila/newmaf/dmel/2L/2Ldel.bed", "r")
d={}
for i in f.readlines():
	if i.startswith("A"):
		d[i.split("\t")([1])]=(int(i.split("\t")[2])-int(i.split("\t")[1]))
