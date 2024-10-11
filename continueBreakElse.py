for i in range(100):
    print(i)
    if i >= 5:
        print('Breaking out of loop.')
        break
print('done')
print('-'*10)

for i in range(1,11):
    if i%2 == 1:
        continue
    print(i)
print('done')
print('-'*10)

for i in range(1,11):
    if i%2 == 0:
        print(i)
print('done')
print('-'*10)

for i in range(1, 5):
    for j in range(1, 5):
        if (i + j)%2 == 1:
            print(f'{i} + {j} is odd, skipping...')
            continue
        print(f'Adding numbers: {i} + {j} = {i + j}')
    print('-'*10)
print('done')
print('-'*10)

for i in range(1, 4):
    for j in range(1, 4):
        if j >= 3:
            break
        print(i,j)
    print('-'*10)
print('done')
print('-'*10)


