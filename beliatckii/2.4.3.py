a = input()
res = a.lower()
gc = res.count('c') + res.count('g')
print(gc/len(a)*100)
