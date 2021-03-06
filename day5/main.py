import math

with open('data.txt', 'r') as f:
    paths = f.read()
    l = paths.split('\n')

seat_id = []
def get_seat_id(data = l):

    for d in data:
        firstRow, lastRow, firstCol, lastCol = 0.0, 127.0, 0.0, 7.0
        for step in d:
            if (step == 'F'):
                lastRow = math.floor((firstRow + lastRow) / 2)
            elif (step == 'B'):
                firstRow = math.ceil((firstRow + lastRow) / 2)
            elif (step == 'R'):
                firstCol = math.ceil((firstCol + lastCol) / 2)
            else:
                lastCol = math.floor((firstCol + lastCol) / 2)
        seat_id.append(firstRow * 8 + lastCol)

    return max(seat_id)

greatest_seat_id = get_seat_id()
print(greatest_seat_id)

for i in range(min(seat_id), max(seat_id) + 1):
    if (i not in seat_id and i+1 in seat_id and i-1 in seat_id):
        print(i)