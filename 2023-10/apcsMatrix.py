from time import sleep

rawSize: str = input("請輸入矩陣大小：")
rawData: str = input("請輸入矩陣資料：")
print("")

# 一堆奇葩的變數
size: list = rawSize.split(" ")
data: list = rawData.split(" ")
numberA: int = None
numberB: int = None
indexA: int = 0
indexB: int = 0
gNumResult: tuple = ()
cNumResult: tuple = ()


def getNum():
    # [!] 第一橫排試做
    numA = data[indexA]
    indexB = indexA
    while True:
        indexB += 1
        if indexB + 1 > int(size[0]):
            return "1"  # 超出範圍 找不到更多資料
        elif data[indexB] != "*":  # 「*」作為空資料替代字元
            numB = data[indexB]
            return "0", numA, numB, indexA, indexB


def checkNum(nA, nB, iA, iB):
    try:
        rRr == 0
    except NameError:
        rRr: int = 0
    if nA == nB:
        data[iA] = "*"
        data[iB] = "*"
        rRr += int(nA)
        return "0", rRr
    else:
        return "1"

while True:
    if int(size[0]) <= 1:
        print("橫排只有一個數字，不做橫排數字配對。")
        break

    gNumResult = getNum()
    if gNumResult[0] == "0":
        cNumResult = checkNum(
            gNumResult[1], gNumResult[2], gNumResult[3], gNumResult[4]
        )
        if cNumResult[0] == "0":
            print('suc')
            if gNumResult[3] == 0:
                indexA += 2
            else:
                indexA -= 1
        else:
            indexA += 1
    else:
        ...
