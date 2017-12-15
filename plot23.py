import csv
import sys

from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib import colors as mcolors

fig = Figure(figsize=[10,5])
ax = Axes(fig, [.1,.1,.8,.8])
fig.add_axes(ax)

f = open(sys.argv[1], 'rb')
reader = csv.reader(f)
your_list = list(reader)
groups = {}

clrs=mcolors.cnames.keys()

for row1 in your_list:
	if not row1[3].isdigit(): continue
	name1=row1[0]
	chro1=row1[2]
	if chro1 == '': continue
	beg1=int(row1[3])
	end1=int(row1[4])
	group1=row1[31]
	if group1 not in groups:
		groups[group1] = clrs[len(groups)]
	color = groups[group1]
	if chro1=='X': chro1=23
	l = Line2D([beg1,end1],[chro1,chro1],color=color,linewidth=10.0)
	ax.add_line(l)

print groups

print 'Lines:', len(your_list)
print 'Groups:', len(groups)
print 'Max Colors:', len(clrs)

ax.set_xlim(0, 250000000)
ax.set_ylim(24, 0)

canvas = FigureCanvasAgg(fig)
canvas.print_figure("all-" + sys.argv[1] + ".png")
