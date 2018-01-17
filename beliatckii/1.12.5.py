a, b, c = int(input()), int(input()), int(input())
mx, mn, md = a, a, a
if b > mx:
    mx = b
elif b < mn:
    mn = b
if c > mx:
    mx = c
elif c < mn:
    mn = c
print(mx)
print(mn)
print((a+b+c)-mx-mn)
