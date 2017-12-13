#!/usr/bin/env python

import csv
import sys

def getOverlap(a, b):
	return max(0, min(a[1], b[1]) - max(a[0], b[0])) / float(min(b[1]-b[0], a[1]-a[0]))

filename=sys.argv[1]

f = open(filename, 'rb')
print "Input:", filename
reader = csv.reader(f)
your_list = list(reader)
elements = len(your_list[0])
print 'elements', elements
your_list[0].append( "Group" );
print len(your_list[0])
print 'LINES', len(your_list)

groups = {}

ofile  = open("grp_" + filename, "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(your_list[0])

minimal_snp=700
minimal_length=7
minimal_overlap=0.1

for row1 in your_list:
	if not row1[3].isdigit(): continue
	name1=row1[0]
	chro1=row1[2]
	if chro1 == '': continue
	beg1=int(row1[3])
	end1=int(row1[4])
	cM1=float(row1[5])
	snp1=int(row1[6])
	#seg1=int(row1[15])
	if snp1 < minimal_snp: continue
	if cM1 < minimal_length: continue

	relatives = set()

	for row2 in your_list:
		if not row2[3].isdigit(): continue
		name2=row2[0]
		chro2=row2[2]
		if chro2 == '': continue
		beg2=int(row2[3])
		end2=int(row2[4])
		cM2=float(row2[5])
		snp2=int(row2[6])
		#seg2=int(row2[15])
		if snp2 < minimal_snp: continue
		if cM2 < minimal_length: continue

		if (chro1 == chro2 and getOverlap([beg1, end1], [beg2, end2]) >= minimal_overlap):
			relatives.add(name2)
	groups.update({name1: relatives})

for k in groups.keys():
	if k in groups:
		for j in groups.keys():
			if k == j: continue
			c = groups[k].intersection(groups[j])
			if bool(c):
				groups[k].update(groups[j])
				del groups[j]

for k in groups.keys():
	if len(groups[k]) > 1:
		print k, groups[k]

for row1 in your_list:
	for k in groups.keys():
		name1=row1[0]
		if name1 in groups[k]:
			row1.append(k)
			writer.writerow(row1)

f.close()
