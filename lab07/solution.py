import numpy as np


def reshape_rows(values: list, width: int) -> list:
    if width <= 0 or len(values) % width != 0:
        return []

    array = np.asarray(values, dtype=float)
    return array.reshape(-1, width).tolist()


def block(matrix: list, rows: list, columns: list) -> list:
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    return array[np.ix_(rows, columns)].tolist()


def column_means(matrix: list) -> list:
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []

    return np.round(array.mean(axis=0), 6).tolist()


def column_range(matrix: list, column: int) -> float:
    if not matrix:
        return 0.0

    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return 0.0

    value = array[:, column].max() - array[:, column].min()
    return round(float(value), 6)
