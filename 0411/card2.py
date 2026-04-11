N = int(input())

queue = list(range(1, N+1))

# print(queue)

for i in range(N-1):
    # 1. 맨 앞의 카드를 버린다.
    queue.pop(0)

    # print(queue)
    # 2. 맨 앞 카드를 제일 아래로 옮기기
    temp = queue.pop(0)
    queue.append(temp)

# 1,2 반복
print(queue.pop())