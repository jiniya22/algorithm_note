"""
여행가 A씨는 N x N 크기의 정사각형 공간 위에 서있습니다.
이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표가 (1, 1) 이고, 가장 오른쪽 아래의 좌표가 (N, N)이라고 하고
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며 시작점은 (1, 1)입니다.

계획서 내에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있습니다.
    - L: 왼쪽으로 한칸 이동
    - R: 오른쪽으로 한칸 이동
    - U: 위쪽으로 한칸 이동
    - D: 아래쪽으로 한칸 이동

첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1 <= N <= 100)
둘째 줄에는 여행가 A가 이동할 계획서 내용이 주어집니다 (1 <= 이동횟수 <= 100)
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (x, y)를 공백을 기준으로 구분하여 출력합니다.
※ 단, 공간 밖을 넘어가는 것은 무시합니다.

입력 예시:
5
R R R U D D

출력 예시:
3 4
"""

N = int(input())
x, y = 1, 1
plans = input().split()

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)