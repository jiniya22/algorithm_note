"""
거스름돈으로 사용 가능한 동전은 500, 100, 50, 10원 짜리 동전이며, 각 동전의 개수는 무한개 있습니다.
손님에게 거슬러줘야할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수는?

첫째 줄 금액 N을 입력받으며, 거슬러줘야할 동전의 최소 개수를 출력하면 됩니다.
입력 예시: 1950
출력: 8
"""

N = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += N // coin
    N %= coin
print(count)