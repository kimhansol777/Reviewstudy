import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. **Titanic 데이터셋 이해**
#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
#    - 데이터 형태: 891행, 15개 열
#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측

def data_titanic():
    df = sns.load_dataset('titanic')
    print(df.info())
    print(df.describe())
#print(data_titanic())

# 2. **좌석 등급별 생존율 분석**
#    - `groupby('pclass')['survived'].mean()` 사용
#    - 예상 결과: 1등석 > 2등석 > 3등석 생존율
#    - 생존율 차이 해석
def place_rank():
    df = sns.load_dataset('titanic')
    df1 = df.groupby('pclass')['survived'].mean()
    return df1
print(place_rank())


# 3. **성별-좌석등급별 다중 집계**
#    - `groupby(['sex', 'pclass']).agg()` 사용
#    - 각 그룹별 나이 평균, 요금 최대값, 생존율 계산
#    - 가장 높은 생존율 그룹 찾기
def sex_place():
    df = sns.load_dataset('titanic')
    #df1 = df.groupby(['sex', 'pclass'])['survived'].agg(['mean', 'max', 'count']) # 이거는 하나의 컬럼을 보고 분석
    df2 = df.groupby(['sex', 'pclass']).agg({'age': 'mean', 'fare': 'max', 'survived': 'mean'}) 
    #'age': 'mean', 'fare': 'max', 'survived': 'mean' 이거는 그거에 대한 컬럼들을 보여준다.
    return  df2
print(sex_place())
# 4. **피벗 테이블 생성**
#    - 성별 × 좌석등급 생존율 피벗 테이블
#    - 히트맵으로 시각화하여 패턴 확인
def pivot_table_single():
     df = sns.load_dataset('titanic')
     df1 = pd.pivot_table(data=df,index = 'sex', columns='pclass', values='survived', aggfunc='mean')
     plt.figure(figsize=(8, 10))
     sns.heatmap(df1, annot=True) # 숫자를 표시하고 싶으면 annot=True 추가
     plt.show()
pivot_table_single()

# 5. **시각화**
#    - 좌석등급별 생존율 막대 그래프
#    - 성별-좌석등급 생존율 히트맵
#    - 연령대별 생존자 수

def pclass_visualization():
    df = sns.load_dataset('titanic')

    plt.figure(figsize=(8, 10))
    sns.barplot(
        data=df,
        x='pclass',
        y='survived'
    )
    plt.show()

    df1 = pd.pivot_table(data=df,index = 'sex', columns='pclass', values='survived', aggfunc='mean')
    plt.figure(figsize=(8, 10))
    sns.heatmap(df1, annot=True) # 숫자를 표시하고 싶으면 annot=True 추가
    plt.show()
    
    plt.figure(figsize=(8, 10))
    df1 = sns.histplot(data=df[df['survived']==1], x='age', bins=20)
    plt.show()
pclass_visualization()
