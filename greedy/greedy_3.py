"""
각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하여
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 만들어라.
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이뤄진다고 가정합니다.

첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어집니다.
만들어질 수 있는 가장 큰 수를 첫번째 줄에 출력하시오.
(1 <= len(S) <= 20)

입력 예시: 02569
출력 결과: 576
(((0 + 2) x 5) x 6) x 2) = 540
"""

S = input()
result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)
