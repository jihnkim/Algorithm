"""
휴식 공간이 적절한 지 판별하는 코드 작성
"""

def need_rest():
    plc_lst = []
    a, b, r = map(int, input('공사현장의 x좌표, y좌표, 공사장 소음 거리를 입력하세요: ').split())
    n = map(int, input('그늘의 수를 입력하세요: ').split())
    for i in range(n):
        x, y = map(int, input().split())
        if (x-a)**2 + (y-b)**2 >= r**2:
            print('silent')
        else:
            print('noisy')

    #     plc = map(int, input(f'{i+1}번 째 그늘의 좌표를 입력하세요: ').split())
    #     plc_lst.append(plc)
    #
    # if (a - plc_lst[i][0])**2 + (b - plc_lst[i][1]) >= r**2:


    # for i in range(n):
    #     print(f'{i+1}번 째의 휴식')

