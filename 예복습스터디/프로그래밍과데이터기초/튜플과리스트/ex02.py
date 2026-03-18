## 주제 3: 튜플과 리스트 컴프리헨션을 활용한 좌표계 데이터 처리
# 주어진 좌표 데이터 (x, y) 형태의 튜플 리스트
points = [(1, 2), (3, 4), (-1, 5), (2, -3), (0, 0), (4, 1), (-2, -2)]



## 문제 

#문제 1: 원점(0,0)으로부터의 거리가 3 이하인 점들만 필터링
"""
- 원점(0,0)으로부터의 거리가 3 이하인 점들만 필터링
    - 거리 공식: sqrt(x^2 + y^2)
"""
def three_below(points):
    return [(x,y) for x,y in points if (x**2+y**2)**0.5 <= 3]


#문제 2: 모든 점을 x축 기준으로 대칭 이동시킨 새로운 좌표 리스트 생성
## 문제 
"""
- 모든 점을 x축 기준으로 대칭 이동시킨 새로운 좌표 리스트 생성
  - x축 대칭: (x, y) -> (x, -y)
"""
def absolute_y(points):
    return [(x,y*-1) for x,y in points ]


#문제 3: 1사분면(x > 0, y > 0)에 있는 점들의 개수 계산
"""
## 문제 
- 1사분면(x > 0, y > 0)에 있는 점들의 개수 계산
"""

def  positives(points):
    return sum([1 for x,y in points if x > 0 and y > 0])


#문제 4: 각 점의 원점으로부터의 거리를 계산한 리스트 생성
"""
## 문제 
- 각 점의 원점으로부터의 거리를 계산한 리스트 생성
  - 거리 공식: sqrt(x^2 + y^2)
"""
def distance_origin(points):
    return [(x**2+y**2)**0.5 for x,y in points]

print(three_below(points))
print(absolute_y(points))
print(positives(points))
print(distance_origin(points))



