# 初始化矩陣
def create_matrix(rows, cols, initial_value=0):
    return [[initial_value for _ in range(cols)] for _ in range(rows)]

# 定義函式，將值存入矩陣的指定位置
def gray(array, i, j, value):
    if 0 <= i < len(array) and 0 <= j < len(array[0]):  # 檢查索引是否在範圍內
        array[i][j] = value
    else:
        print(f"索引 ({i}, {j}) 超出範圍！")

# 定義顯示函式
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:3}" for val in row))

# 測試
rows, cols = 5, 5
image = create_matrix(rows, cols)

gray(image, 0, 1, 50)
gray(image, 1, 3, 120)
gray(image, 2, 4, 180)
gray(image, 3, 2, 255)

# 顯示結果
print("稀疏矩陣存儲結果：")
print_matrix(image)
