x = int(input())
h = int(input())
m = int(input())

h2 = x // 60
m2 = x % 60
m3 = (m2+m) % 60
h3 = (m2+m) // 60
h4 = h + h2 + h3
print(h4)
print(m3)
