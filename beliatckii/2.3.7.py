a, b = int(input()), int(input())
s, j = 0, 0
for i in range(a, b+1):
	if i%3 == 0:
		s = s+i
		i+=1
		j+=1
	else:
		i+=1
print(s/j)
