stack = []

stack.append(5)
stack.append(3)
stack.append(13)
stack.append(1)
stack.pop()
stack.append(2)
stack.append(44)
stack.pop()

print(stack[::-1])  # 맨 위부터 출력
print(stack)    # 맨 아래부터 출력

"""
출력 결과:
[2, 13, 3, 5]
[5, 3, 13, 2]
"""