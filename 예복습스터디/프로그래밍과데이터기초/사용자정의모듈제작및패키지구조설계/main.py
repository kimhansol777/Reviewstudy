"""
points = [(1, 2), (3, 4), (-1, 5), (2, -3), (0, 0), (4, 1), (-2, -2)]

문제 3-1
#- 원점(0,0)으로부터의 거리가 3 이하인 점들만 필터링
거리 공식: sqrt(x^2 + y^2)
import math

result=[]

for x, y in points:
    if math.sqrt(x2 + y2) <= 3:
        result.append((x, y))

print(result)

문제 3-2
모든 점을 x축 기준으로 대칭 이동시킨 새로운 좌표 리스트 생성
x축 대칭: (x, y) -> (x, -y)
import math

result = []
for x, y in points:
    result.append((x, -y))

print(result)

문제 3-3
1사분면(x > 0, y > 0)에 있는 점들의 개수 계산
import math

result = []
for x, y in points:
    if x > 0 and y > 0:
        result.append((x, y))

print(len(result))

문제 3-4
각 점의 원점으로부터의 거리를 계산한 리스트 생성
거리 공식: sqrt(x^2 + y^2)
import math

result = []
for x, y in points:
    result.append(math.sqrt(x2 + y2))

print(result)
"""