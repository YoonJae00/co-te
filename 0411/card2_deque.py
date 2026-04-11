from collections import deque
N = int(input())

queue = deque(range(1, N+1))
# print(queue)

for i in range(N-1):
    # 1. 맨 앞의 카드를 버린다.
    queue.popleft()

    # print(queue)
    # 2. 맨 앞 카드를 제일 아래로 옮기기
    temp = queue.popleft()
    queue.append(temp)

# 1,2 반복
print(queue.pop())