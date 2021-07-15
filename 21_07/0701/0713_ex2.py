"""
Queue : 대기열
FIFO 선입선출
pop = dequeue
push = enqueue
empty
"""

"""
push X : 정수 x를 큐에 넣는 연산
pop : 가장 front 숫자 출력하고 빼내기 없으면 -1
size : queue에 있는 정수 개수 출력
empty : 비어있는지 유무 1, 0
front : 큐의 가장 앞의 정수 출력 없으면 -1
back : 가장 뒷 정수 출력 없으면 -1

"""

class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.queue_size = 0
        self.front_index = 0
        self.back_index = -n

    def push(self, num):
        self.queue[self.back_index] = int(num)
        self.queue_size += 1
        self.back_index += 1

    def pop(self):
        if self.queue_size > 0:
            val = self.queue[self.front_index]
            self.queue[self.front_index] = None
            self.queue_size -= 1
            self.front_index += 1
            return val
            
        return -1
    
    def size(self):
        return self.queue_size

    def empty(self):
        if self.queue_size > 0:
            return 0
        
        return 1

    def front(self):
        if self.queue_size > 0:
            return self.queue[self.front_index]
            
        return -1

    def back(self):
        if self.queue_size > 0:
            return self.queue[self.back_index-1]
            
        return -1
    
def run_cmd(my_queue, cmd):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd
        my_queue.push(num)
    elif cmd_type == "pop":
        print(my_queue.pop())
    elif cmd_type == "size":
        print(my_queue.size())
    elif cmd_type == "empty":
        print(my_queue.empty())
    elif cmd_type == "front":
        print(my_queue.front())
    elif cmd_type == "back":
        print(my_queue.back())

    return my_queue

n = int(input('integer : '))
my_queue = Queue(n)

for _ in range(n):
    command = input('input command : ').split()
    run_cmd(my_queue, command)
    print(my_queue.queue)
    print(f'My Queue size: {my_queue.queue_size}')