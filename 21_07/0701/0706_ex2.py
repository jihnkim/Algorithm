


def process_stack(stack, stack_size, command):
    if command[0] == 'push':
        stack.append(command[1])
        stack_size += 1

    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[stack_size-1])
            stack.pop()
            stack_size -= 1

    elif command[0] == 'top':
        print(stack[stack_size-1])

    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    else:
        new_stack = stack.copy()
        print(new_stack.index(stack.pop())+1)

    return stack, stack_size

n = int(input('명령의 수를 입력하세요 : '))

for _ in range(n):
    command = input('명령을 입력하세요 : ').split(" ")
    print(command)
    stack, stack_size = process_stack(stack, stack_size, command)
    if _ == n-1:
        print('end')
        break
