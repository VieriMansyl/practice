def generateMatrix(n: int) -> list[list[int]]:
    mat = [[0 for _ in range(n)] for _ in range(n)]

    num = 1

    startRow, endRow = 0, n-1
    startCol, endCol = 0, n-1

    while num <= n*n:
        for i in range(startCol, endCol+1, 1):
            mat[startRow][i] = num
            num += 1
        startRow += 1

        for i in range(startRow, endRow+1, 1):
            mat[i][endRow] = num
            num += 1
        endCol -= 1

        for i in range(endCol, startCol-1, -1):
            mat[endRow][i] = num
            num += 1
        endRow -= 1

        for i in range(endRow, startRow-1, -1):
            mat[i][startRow-1] = num
            num += 1
        startCol += 1
    return mat

print(generateMatrix(1))