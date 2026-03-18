import numpy as np
import pandas as pd

# 1. 다음 벡터를 생성하고 내적 계산
#    -
#    - np.dot() 또는 @ 연산자 사용
#    - 결과 출력 및 수동 검증

def scalar_product():
    v1 = [1, 2, 3, 4]
    v2 = [5, 6, 7, 8]
    v1 = np.array(v1)
    v2 = np.array(v2)
    return v1 @ v2



# 2. 행렬 곱셈 수행
#    - 2×3 행렬 A와 3×2 행렬 B 생성
#    - A @ B 계산 (결과: 2×2 행렬)

def mul_product():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8], [9, 10], [11, 12]])
    return a @ b

# 3. 벡터 노름 계산
#    - 벡터 c = [3, 4, 5]에 대해
#    - L1, L2, L∞ 노름 모두 계산
#    - np.linalg.norm() 사용
def norms(n):
    c = np.array([3, 4, 5])
    return np.linalg.norm(c, n)


# 4. 조건부 인덱싱
#    - 배열 data = [1, 5, 3, 8, 2, 9, 4, 7, 6]
#    - 5보다 큰 값 추출
#    - 3 이상 7 이하 값 추출
#    - 짝수 값 추출
def indexings()->list:
    data = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])

    cond = data > 5
    cond1 = (data >= 3) & (data <= 7)
    cond2 = data % 2 == 0
    new_data = data[cond],data[cond1],data[cond2]
    new_data = tuple(arr.tolist() for arr in data)
    return new_data
    
    
print(scalar_product())
print(mul_product())
print(norms(10))

print(indexings())