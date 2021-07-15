class Stack():
    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def push(self, num):
        self.stack.append(int(num))
        self.stack_size += 1

    def pop(self):
        if self.stack:
            self.stack_size -= 1
            return self.stack.pop()

        return -1

    def size(self):
        return self.stack_size

    def empty(self):
        if self.stack_size>0:
            return 0

        return 1

    def top(self):
        if self.stack_size>0:
            return self.stack[self.stack_size]

        return -1

def run_stack_cmd():

    return my_stack

my_stack = Stack()
n = int(input())

for _ in range(n):
    command = input('명령을 입력하세요 : ').split(" ")
    print(command)
    my_stack = run_stack_cmd(my_stack, command)

