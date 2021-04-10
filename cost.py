# import itertools

def A(values, d): 
	s = 0
	for i in range(len(values)):
		p = 0
		for j in range(i+1):
			p+= values[j][1]
		s += values[i][0] * abs(p - d)
	return s

# def d(values):
# 	n = sum(values)
# 	i = 0
# 	s = values[0]
# 	while s < n/2:
# 		i+=1
# 		s+=values[i]
# 	return i, sum(values[:i+1])

# values = [(4, 8), (7, 11), (9, 5), (6, 15)]
# d = 24
values = [(6, 15), (7, 11), (9, 5), (4, 8)]
d = 26
# values = [(1, 1)]*10
# for d in [4, 4.5, 5, 5.5, 6, 6.5]:
print(A(values, d))

# pers = itertools.permutations(values)
# m_a = -1
# mins = []

# for per in pers:
# 	d_p = d(per)
# 	a = A(per, d_p[1])
# 	if m_a == -1 or a < m_a:
# 		m_a = a
# 		mins = [(per, d_p)]
# 	elif m_a == a:
# 		mins.append((per, d_p))
# 	# print("Permutation : ", *per, "Pizza on the 0: ", *d_p, "Cost : ", A(per, d_p[1]))

# print("Minimal cost :", a)
# for per, d_p in mins:
# 	print("Perm:", *per, "\t Pizza on 0:", *d_p)