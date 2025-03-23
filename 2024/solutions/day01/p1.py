with open('resources/input.txt', 'r') as file:
    first_col, second_col = [], []
    for line in file.readlines():
        _first_col, _second_col = line.split('   ')
        first_col.append(int(_first_col))
        second_col.append(int(_second_col))

    first_col.sort()
    second_col.sort()

    distances = []
    for i, num in enumerate(first_col):
        distance = abs(num - second_col[i])
        distances.append(distance)

    print(sum(distances))