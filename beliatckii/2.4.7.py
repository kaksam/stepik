s = input()
i = 0
c = 1
out = ''
while i< (len(s) - 1):
    if s[i] == s[i+1]:
        c += 1
    else:
        out = out + s[i] + str(c)
        c = 1
    i +=1
print(out+ s[i] + str(c))
