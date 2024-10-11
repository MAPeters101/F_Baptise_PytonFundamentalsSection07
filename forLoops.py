suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

for suit in suits:
    print(suit)
print()

for suit in suits:
    abbrev = suit[0].upper()
    print(f'{abbrev} = {suit}')
print()

for suit in suits:
    print(f'{suit[0].upper()} = {suit}')
print(suit)
print()

for c in 'python':
    print(c)
print(c)
print()

for i in range(2, 11, 2):
    print(i)
print(list(range(2, 11, 2)))
print()

for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
    print('-'*10)


m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row_idx in range(3):
    for col_idx in range(3):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')

print(len(m))
print(len(m[0]))
print()


for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print()

m = [
    [0, 1],
    [2,3,4,5,6],
    [7,8,9],
    [10]
]
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print()

n=5
matrix=[]
for row_idx in range(n):
    row=[]
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)
print()

n=10
matrix=[]
for row_idx in range(n):
    row=[]
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)
print()

data = [10, 20, 30]
print(enumerate(data))
print(list(enumerate(data)))
print()

for t in enumerate(data):
    print(t)
print()

for t in enumerate(data):
    idx, el = t
    print(idx, el)
print()

for idx, el in enumerate(data):
    print(idx, el)
print()

m = [
    [0, 1],
    [2,3,4,5,6],
    [7,8,9],
    [10]
]
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}')
print()

for row in m:
    for element in row:
        print(element)
print()

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(m[row_idx][col_idx])
print()

for row_idx, row in enumerate(m):
    print(row_idx, row)
print()

for row_idx, row in enumerate(m):
    for col_idx, element in enumerate(row):
        print(row_idx, col_idx, element)
print()

for row_idx, row in enumerate(m):
    for col_idx, element in enumerate(row):
        print(f'[{row_idx}, {col_idx}] = {element}')
print()






