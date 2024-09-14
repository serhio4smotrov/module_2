n = int(input('Пароль первой вставки: '))
summ = []
result = ''
if 3 <= n <= 20:
    for i in range(1,n):
        for j in range(1,n):
            if n % (i + j) == 0 and summ.count(sorted([i, j])) < 1 and i != j:
                summ.append(sorted([i, j]))
                result = result + f'{i},{j}  '
    print(f'Пароль второй вставки: {result}')
else:
    print('Нет такого значения на первой вставке')