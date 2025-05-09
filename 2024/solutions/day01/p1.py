def extract_columns_from_file(path: str) -> tuple[list, list]:
    first_col, second_col = [], []
    with open(path, 'r') as file:
        for line in file.readlines():
            first_item, second_item = line.split('   ')
            first_col.append(int(first_item))
            second_col.append(int(second_item))
    return first_col, second_col


def resolve():
    first_col, second_col = extract_columns_from_file('resources/input.txt')
    first_col.sort()
    second_col.sort()

    distances = []
    for i, num in enumerate(first_col):
        distance = abs(num - second_col[i])
        distances.append(distance)

    print(sum(distances))


if __name__ == "__main__":
    resolve()