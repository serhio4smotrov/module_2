n = int(input('Пароль первой вставки: '))
result = ''
for i in range(1, n):
     for j in range(i + 1, n):
        if n % (i + j) == 0:
            result = result + f'{i},{j}  '
print(f'Пароль второй вставки: {result}')