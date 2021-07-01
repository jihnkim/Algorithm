
a, b, r = map(int, input('공사현장의 x좌표, y좌표, 공사장 소음 거리를 입력하세요: ').split())
n = int(input('그늘의 수를 입력하세요: '))

for i in range(0, n):
    x, y = map(int, input().split())
    if (x - a) ** 2 + (y - b) ** 2 >= r ** 2:
        print('silent')
    else:
        print('noisy')