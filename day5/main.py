import math

with open('data.txt', 'r') as f:
    paths = f.read()
    l = paths.split('\n')

def get_seat_id(data = l):
    seat_id = []

    for d in data:
        firstRow, lastRow, firstCol, lastCol = 0.0, 127.0, 0.0, 7.0
        print(d)
        for step in d:
            # print(step)
            if (step == 'F'):
                print('F')
                lastRow = math.floor((firstRow + lastRow) / 2)
            elif (step == 'B'):
                print('B')
                firstRow = math.ceil((firstRow + lastRow) / 2)
            elif (step == 'R'):
                print('R')
                firstCol = math.ceil((firstCol + lastCol) / 2)
            else:
                print('L')
                lastCol = math.floor((firstCol + lastCol) / 2)
        # print(firstRow, lastCol)
        seat_id.append(firstRow * 8 + lastCol)

        # print(seat_id)


    return max(seat_id)

greatest_seat_id = get_seat_id()
print(greatest_seat_id)