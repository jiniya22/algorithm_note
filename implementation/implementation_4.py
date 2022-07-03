"""
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 모든 숫자를 더한값을 이어서 출력합니다

첫째 줄에 하나의 문자열 S가 주어집니다(1 <= S의 길이 <= 10,000)
첫째 줄에 결과를 출력합니다.

입력 예시:
AJKDLSI412K4JSJ9D

출력 예시:
ADDIJJJKKLSS20
"""

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print("".join(result))
