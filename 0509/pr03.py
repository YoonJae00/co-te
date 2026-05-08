# https://jungol.co.kr/problem/4189?cursor=OCw3LDA=

# bfs

X, Y = map(int, input().split())
H_X, H_Y, Z_X, Z_Y = map(int, input().split())

from collections import deque

# 방문위치 체크
visited = [[False] * (Y + 1) for _ in range(X + 1)]

queue = deque()


# 이동위치, 이동횟수
queue.append((H_X, H_Y, 0))

visited[H_X][H_Y] = True

# 말 이동방향
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


while queue:
    x, y, count = queue.popleft()

    # 졸 위치 도착
    if x == Z_X and y == Z_Y:
        print(count)
        break

    # 8방향 탐색
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안인지 확인
        if 1 <= nx <= X and 1 <= ny <= Y:

            # 방문 안 했으면
            if not visited[nx][ny]:
                visited[nx][ny] = True

                # 다음 위치 + 이동횟수 1 증가
                queue.append((nx, ny, count + 1))