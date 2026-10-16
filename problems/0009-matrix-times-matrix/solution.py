def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    I,J,K = len(a),len(a[0]),len(b)

    c = []
    for i in range(I):
        temp = []
        for k in range(K):
            temp.append(0)
        c.append(temp)

    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][k] += a[i][j] * b[j][k]
    return c