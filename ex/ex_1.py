# N으로 나누었을 때 나머지와 몫이 같은 경우 그 때의 모든 자연수의 합
def solve_ex1(n):
    num = []
    lst = []
    # n = int(input('자연수 N의 값을 설정해 주세요 '))

    for i in range(1, n ** 2):
        num.append(i)
        a = num[i - 1] % n
        b = num[i - 1] // n
        if a == b:
            lst.append(num[i - 1])

    return print(sum(lst))

def solve_ex2(n):
    res = 0
    for i in range(1, n):
        res += (i*n) + 1


# -------------------------------------------
# n = int(input())
# s = 0
# for i in range(n+1,n**2,n+1):
#   s += i
# print(s)