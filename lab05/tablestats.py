def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        values = line.split(",")
        for i in range(len(values)):
            values[i] = values[i].strip()

        if not header:
            header = values
            continue

        if len(values) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]
        rows.append(row)

    return rows
