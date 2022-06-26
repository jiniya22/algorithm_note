"""
어떠한 수 N이 1이 될때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려 한다.
    1. N에서 1을 뺀다.
    2. N에서 K로 나눈다.
단, 두번째 연산은 N이 K개로 나누어 떨어질 때만 선택할 수 있다.

첫째 줄에 N과 K가 공백을 기준으로 하여 각각 자연수로 주어진다.
N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야하는 회수의 최솟값을 출력하라.
(1<=N<=100,000, 2<=K<=100,000)
입력 예시: 25 3
출력: 6
"""

N, K = map(int, input().split())
count = 0

while True:
    target = N // K * K
    count += (N - target)
    N = target
    if N < K:
        break
    count += 1
    N //= K

count += (N - 1)
print(count)
