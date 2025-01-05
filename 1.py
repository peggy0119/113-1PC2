第一題
# 定義多項式的係數 (按次數從高到低排列)
coefficients = [6, 0, 2, 0, 3]  # 6x^4 + 0x^3 + 2x^2 + 0x + 3

def evaluate_polynomial(coeffs, x):
    """計算多項式的值"""
    return sum(c * (x ** i) for i, c in enumerate(reversed(coeffs)))

# 計算 x = 91 時的值
x = 91
result = evaluate_polynomial(coefficients, x)

# 顯示結果
print(f"f({x}) = {result}")

第二題
class Polynomial:
    """多項式 (如 f(x) = 6x^4 + 2x^2 + 3)"""
    def __init__(self, coefficients):
        """
        初始化多項式
        :param coefficients: 按次數從高到低排列的係數列表
        """
        self.coefficients = coefficients

    def evaluate(self, x):
        """計算多項式的值"""
        return sum(c * (x ** i) for i, c in enumerate(reversed(self.coefficients)))

    def __str__(self):
        """返回多項式的字串表示形式"""
        terms = []
        degree = len(self.coefficients) - 1
        for i, c in enumerate(self.coefficients):
            if c == 0:
                continue
            power = degree - i
            if power == 0:
                terms.append(f"{c}")
            elif power == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{power}")
        return " + ".join(terms)

# 建立多項式 f(x) = 6x^4 + 2x^2 + 3
f = Polynomial([6, 0, 2, 0, 3])

# 顯示多項式
print(f"Polynomial: {f}")

# 計算 x = 91 時的值
x = 91
result = f.evaluate(x)

# 顯示結果
print(f"f({x}) = {result}")
