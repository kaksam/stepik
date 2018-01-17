a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(end='\t')
for i in range(c, d+1):
    print(i, end='\t')
print('')
for i in range(a, b + 1):
    print(i,end='\t')
    for j in range(c,d+2):
        print(i*j,end='\t')
        j+=1
        if j == d+1:
            print('')
            break
    i+=1
