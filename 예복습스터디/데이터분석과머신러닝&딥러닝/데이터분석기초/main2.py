import pandas as pd
import numpy as np


# 1. **DataFrame 생성 및 기본 정보 확인**
#    - 딕셔너리로부터 DataFrame 생성 (8명의 직원 데이터)
#    - 속성: 이름, 나이, 도시, 급여, 부서, 경력
#    - `df.info()`, `df.describe()` 사용하여 데이터 개요 파악
data = {
        'name': ['김철수', '이영희', '박민수', '최지영', '정태현', '한소희', '윤상호', '배수진'],
        'age': [25, 30, 35, 28, 42, 31, 29, 27],
        'city': ['서울', '부산', '대구', '서울', '광주', '서울', '부산', '대구'],
        'salary': [3500, 4200, 3800, 4500, 5200, 3900, 3600, 4100],
        'department': ['개발', '마케팅', '개발', '기획', '개발', '마케팅', '기획', '개발'],
        'experience': [2, 5, 8, 3, 12, 6, 4, 3]
    }
def data_info():
    df = pd.DataFrame(data)
    print(df.info())
    print(df.describe())


# 2. **단일 조건 필터링**
#    - 나이가 30 이상인 직원 추출
#    - 특정 도시(예: 서울) 거주 직원 찾기
#    - 급여가 4000 이상인 직원 필터링
def filters():
    df = pd.DataFrame(data)
    df1 = df[df['age'] >= 30]
    df2 = df[df['city'] == '서울']
    df3 = df[df['salary'] >= 4000]
    return df1, df2, df3




# 3. **복합 조건 필터링**
#    - AND 연산: 서울 거주 **AND** 급여 4000 이상
#    - OR 연산: 개발팀 **OR** 급여 4500 이상
#    - NOT 연산: 개발팀이 아닌 직원
def mul_filters():
    df = pd.DataFrame(data)
    df1 = df[(df['city'] == '서울') & (df['salary'] >= 4000)]
    df2 = df[(df['department'] == '개발') | (df['salary'] >= 4500)]
    df3 = df[df['department'] != '개발']
    return df1, df2, df3


# 4. **기본 통계 및 집계**
#    - 부서별 평균 급여 계산
#    - 도시별 직원 수
#    - 경력 통계 분석
def statistics():
    df = pd.DataFrame(data)
    df1 = df.groupby('department')['salary'].mean()
    df2 = df.groupby('city')['name'].count()
    df3 = df.groupby('experience').describe()
    return df1, df2, df3


print(data_info())
print(filters())
print(mul_filters())
print(statistics())