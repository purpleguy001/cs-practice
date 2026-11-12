import numpy as np


# задание 1. создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# задание 2. индексы и срезы вектора
print("third element:", hours[2])
print("last element:", hours[-1])
print("indexes 2-5:", hours[2:6])
print("every second:", hours[::2])
print("reverse:", hours[::-1])


# задание 3. строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("temperatures shape:", temperatures.shape)
print("temperatures ndim:", temperatures.ndim)
print("temperatures size:", temperatures.size)
print("second row, third column:", temperatures[1, 2])
print("first row:", temperatures[0])
print("last column:", temperatures[:, -1])
print("first two rows without first column:\n", temperatures[:2, 1:])
central = temperatures[:2, 1:3]
print("central fragment:\n", central)
print("central shape:", central.shape)


# задание 4. прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)

part = matrix[:3, :]
print("first three rows:\n", part)
print("shape:", part.shape)

part = matrix[-2:, :]
print("last two rows:\n", part)
print("shape:", part.shape)

part = matrix[:, :2]
print("first two columns:\n", part)
print("shape:", part.shape)

part = matrix[1:4, 2:5]
print("rows 1-3, columns 2-4:\n", part)
print("shape:", part.shape)

part = matrix[-2:, -2:]
print("bottom-right block:\n", part)
print("shape:", part.shape)


# задание 5. изменение массива с помощью срезов
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector example:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small matrix example:\n", small_matrix)

# copy() нужна, чтобы изменения changed_hours не меняли исходный hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print("changed_hours:", changed_hours)
print("hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed matrix:\n", changed_matrix)
print("matrix:\n", matrix)


# задание 6. изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers shape:", numbers.shape)
print("table shape:", table.shape)
print("transposed shape:", transposed.shape)
print("table:\n", table)
print("transposed:\n", transposed)

# reshape(3, 4) работает: 3 * 4 = 12 элементов.
# reshape(5, 3) вызовет ошибку: 5 * 3 = 15, а элементов только 12.
