x, y, z = float(input()), float(input()), input()
if z == str('+'):
	print(x+y)
elif z == str('-'):
	print(x-y)
elif z == str('*'):
	print(x*y)
elif z == str('/'):
	if y == 0:
		print('Деление на 0!')
	else:
		print(x/y)
elif z == str('mod'):
	if y == 0:
		print('Деление на 0!')
	else:
		print(x%y)
elif z == str('pow'):
	print(x**y)
elif z == str('div'):
	if y == 0:
		print('Деление на 0!')
	else:
		print(x//y)
