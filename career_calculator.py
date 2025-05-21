def best_career(input_file_name, output_file_name):
    with open(input_file_name) as f:
        L = int(f.readline())
        E = [list(map(int, f.readline().split())) for _ in range(L)]

    for i in range(L - 2, -1, -1):
        for j in range(len(E[i])):
            E[i][j] += max(E[i+1][j], E[i+1][j+1])

    with open(output_file_name, 'w') as f:
        f.write(str(E[0][0]) + '\n')

best_career("lab_6/career.in", "lab_6/career.out")
