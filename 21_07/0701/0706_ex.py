"""
Stack?
LIFO : Last In First Out (후입 선출)
"""
stack = []

def process_stack(command):

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif command[0] == 'top':
        print(stack[-1])

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    else:
        print(len(stack))



n = int(input('명령의 수를 입력하세요 : '))

for _ in range(n):
    command = input('명령을 입력하세요 : ').split(" ")
    print(command)
    process_stack(command)
    if _ == n-1:
        print('end')
        break
