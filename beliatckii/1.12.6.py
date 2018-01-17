a = int(input())
st = 'программист'
ta = 'программиста'
ov = 'программистов'
if 1000 >= a >= 0:
    if a == 0:
        print(str(a), ov)
    elif (a % 10 >= 5 and a % 10 <= 9) or (a % 100 >= 10 and a % 100 <= 20):
        print(str(a), ov)
    elif a%10 >=2 and a%10 <= 4:
        print(str(a), ta)
    elif a%10 == 0:
        print(str(a), ov)
    else:
        print(str(a), st)
