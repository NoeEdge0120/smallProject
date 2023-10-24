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

numA: int = 0
numB: int = 0

nowData = matrix[0].spilt()

numA = nowData[0]
nowIndex: int = 0
while True:
    if nowData[0] != ' ':
        numB = nowData[nowIndex]
        break
    elif nowIndex + 1 >= row:
        break
    else:
        nowIndex += 1
if numA == numB:
    # 數字配對 清除資料 增加至答案 刪除原資料
    