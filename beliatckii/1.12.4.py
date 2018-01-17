x = input()
if x == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a+b+c)/2
    s = (p*((p-a)*(p-b)*(p-c)))**0.5
    print(s)
elif x == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a*b)
elif x == 'круг':
    a = int(input())
    print(3.14 * a**2)

