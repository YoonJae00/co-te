# https://jungol.co.kr/problem/1695?cursor=OCw2LDA=

# 지도 크기
N = int(input())

# 지도 입력
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 단지 집 개수 저장
result = []


# DFS 함수
def dfs(x, y):
    # 현재 집 방문 처리
    graph[x][y] = 0

    # 현재 집 포함
    count = 1

    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안인지 확인
        if 0 <= nx < N and 0 <= ny < N:

            # 집이 있으면 계속 탐색
            if graph[nx][ny] == 1:
                count += dfs(nx, ny)

    return count


# 전체 지도 탐색
for i in range(N):
    for j in range(N):

        # 집 발견하면 새로운 단지 시작
        if graph[i][j] == 1:
            result.append(dfs(i, j))

# 오름차순 정렬
result.sort()

# 총 단지 수
print(len(result))

# 각 단지 집 수 출력
for r in result:
    print(r)