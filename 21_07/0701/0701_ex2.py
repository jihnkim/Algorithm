"""
최대 최소 값 구하기
"""

# lst = []
# n_lst = []
#
# while True:
#     a = input('정수를 입력하세요. 입력이 끝났으면 q를 눌러주세요 : ')
#     if a == 'q':
#         break
#
#     a = int(a)
#     lst.append(a)


#
num_lst = list(map(int, input().split()))
print(num_lst)

max = num_lst[0]
min = num_lst[0]

for n in range(len(num_lst)):
    if max <= num_lst[n]:
        max = num_lst[n]

    if min >= num_lst[n]:
        min = num_lst[n]

print(max)
print(min)

