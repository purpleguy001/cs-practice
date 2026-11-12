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
