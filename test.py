# values = [(2, 19), (3, 13), (6, 18), (18, 18), (15, 12), (14, 7), (5, 2), (6, 9), (6, 14), (2, 13)]
# d = 89
import matplotlib.pyplot as plt
import os
from ast import literal_eval

def analyse(values, d):
	before = 0
	after = 0
	i = 0
	s = 0
	while s < d:
		s += values[i][1]
		i += 1
	i-=1
	before = values[i-1][0] * (values[i][1] - values[i-1][1])
	after = values[i+1][0] * (values[i][1] - values[i+1][1])
	b = values[i-2][0] * (values[i][1] + values[i-1][1] - values[i+1][1] - values[i-2][1])
	a = values[i+2][0] * (values[i-2][1] + values[i-1][1] - values[i+1][1] - values[i+2][1])
	return (before, b, a, after)

def A(values, d): 
	s = 0
	for i in range(len(values)):
		p = 0
		for j in range(i+1):
			p+= values[j][1]
		s += values[i][0] * abs(p - d)
	return s

def rangef(start, end, step):
	x = start
	while (step >0 and x < end) or (step < 0 and x > end):
		yield x
		x+= step

dirs = os.listdir("data")
print(dirs)
# dirs = ["tfjm_10_2021041000125012"]
for file in dirs:
	if (file == "old"): continue
	print(file)
	with open("data/"+file) as f:
		lines = f.readlines()

	dos = []
	values = []
	for line in lines:
		l = line.split(";")
		values.append(literal_eval(l[0]))
		dos.append(int(l[1]))

	for i, value in enumerate(values):
		costs = []
		ds = []
		plt.subplots()
		total = 0
		for pi, di in value: total += di
		for d in rangef(total, -1, -.1):
			costs.append(A(value, round(d,2)))
			ds.append(round(d,2))
		m = -1
		for j in range(len(costs)):
			if m == -1 or costs[j] < costs[m]:
				m = j
		print(ds[m], dos[i])
		plt.plot(ds, costs)
		plt.ylabel("Cost")
		plt.xlabel("Decalage")
		plt.scatter(dos[i], A(value, dos[i]), marker='o', color='r', label='Minimum')
		plt.savefig("images/graphs/"+file+'_'+str(i+1)+".png")
		# plt.show()
		# b1, b2, a2, a1 = (analyse(value, do))
		# print(b1, a1)
		# print(b2, a2)
		# if (b1 > a1): print("Hmmmmmmmmmm...........")
		# if (b2 > a2): print("Hmmmmmmmmmm...........")