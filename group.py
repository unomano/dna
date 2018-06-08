import csv
import sys

def getOverlap(a, b):
	return max(0, min(a[1], b[1]) - max(a[0], b[0])) / float(min(b[1]-b[0], a[1]-a[0]))

filename=sys.argv[1]

f = open(filename, 'rb')
print "Input:", filename
reader = csv.reader(f)
your_list = list(reader)
print 'Group name element:', len(your_list[0])
print 'Lines:', len(your_list)

f2 = open('vfp.csv', 'rb')
reader2 = csv.reader(f2)
vfp_list = list(reader2)

f3 = open('nkk.csv', 'rb')
reader3 = csv.reader(f3)
nkk_list = list(reader3)

ofile  = open("grp_" + filename, "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
your_list[0].pop(8)
your_list[0].insert(3,"Pat")
your_list[0].insert(4,"Mat")
writer.writerow(your_list[0])

for row1 in your_list:
	if not row1[3].isdigit(): continue
	name1=row1[0]
	chro1=row1[2]
	if chro1 == '': continue
	beg1=int(row1[3])
	end1=int(row1[4])
	res = "Vera"
	res2 = "Petr"

	for row2 in vfp_list:
		if not row2[0].isdigit(): continue
		chro2=row2[0]
		beg2=int(row2[1])
		end2=int(row2[2])
		#print chro1, beg1, end1, chro2, beg2, end2

		if (chro1 == chro2 and getOverlap([beg1, end1], [beg2, end2]) >= 1.0):
			res = "Wkrt"

	for row2 in nkk_list:
		if not row2[0].isdigit(): continue
		chro2=row2[0]
		beg2=int(row2[1])
		end2=int(row2[2])
		#print chro1, beg1, end1, chro2, beg2, end2

		if (chro1 == chro2 and getOverlap([beg1, end1], [beg2, end2]) >= 1.0):
			res2 = "Nina"
	
	row1.pop(8)
	row1.insert(3,res)
	row1.insert(4,res2)
	writer.writerow(row1)

f.close()
f2.close()
f3.close()

