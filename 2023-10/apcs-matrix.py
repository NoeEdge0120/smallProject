inp = input('設定二維矩陣大小：')

rule = inp.split()

row: int = int(rule[0])  # 橫排
column: int = int(rule[1])  # 直排

data = input('輸入矩陣資料：')

lData = data.split()
temp: str = ''
x: int
y: int
result: str = ''
index: int = 0

print(lData)

dataNo: int = 0

matrix: dict = {}

for x in range(column):
    print('\n')
    temp: str = ""
    x += 1
    for y in range(row):
        temp = f'{temp} {lData[index]}'
        index += 1
    # result = f'{result} \n {temp}'

    temp.strip(' ')
    matrix[x] = temp

    print(f'x={x} y={y}\nlData: {lData}\ntemp: {temp}\nmatrix: {matrix}')
