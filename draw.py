import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from ast import literal_eval
import os

#values = [(3, 18), (6, 20), (15, 10), (19, 10), (20, 3), (16, 8), (8, 5), (6, 13), (2, 8), (1, 4)]
#d = 61
# values = [(6, 15), (7, 11), (9, 5), (4, 8)]
# d = 31
# values = [(6, 15), (7, 11), (9, 5), (4, 8)]
# d = 26

def draw(values, d, fileName):
	_, ax = plt.subplots()
	x = -d
	m = .2
	for pi, di in values:
		ax.add_patch(Rectangle((x+m, -2.5), di-2*m, 5, 0))
		cx = x + (di/2)
		cy = 0
		ax.annotate("{}\n({})".format(pi, round(pi/di,2)), (cx, cy), color='w', weight='bold', 
					fontsize=6, ha='center', va='center')
		x+=di
	plt.axis([-d-1,x+1,-3,3])
	plt.savefig('images/pizzas/'+fileName)

dirs = os.listdir("data")
print(dirs)
for file in dirs:
	if (file == "old"): continue
	with open("data/"+file) as f:
		lines = f.readlines()
	print(lines)

	ds = []
	values = []
	for line in lines:
		l = line.split(";")
		values.append(literal_eval(l[0]))
		ds.append(int(l[1]))
	print(*values)
	print(*ds)

	for i, value in enumerate(values):
		draw(value, ds[i], file+'_'+str(i+1)+'.png')
