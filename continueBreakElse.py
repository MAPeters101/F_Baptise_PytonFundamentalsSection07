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

i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i)


data = [1, 2, 3, -4, 5, 6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break
if all_positive:
    print('processing all positive elements')


for i in range(5):
    print(i)
else: # no break
    print('loop terminated normally (no break)')

for i in range(5):
    print(i)
    if i > 3:
        break
else: # no break
    print('loop terminated normally (no break)')


data = [1, 2, 3, -4, 5, 6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break
if all_positive:
    print('processing all positive elements')


data = [1, 2, 3, -4, 5, 6]
for element in data:
    if element <= 0:
        break
else:
    print('processing all positive elements')

data = [1, 2, 3, 4, 5, 6]
for element in data:
    if element <= 0:
        break
else:
    print('processing all positive elements')

