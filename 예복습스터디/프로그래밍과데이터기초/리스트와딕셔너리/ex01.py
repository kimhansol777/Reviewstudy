
"""
[전제] 주어진 데이터 구조를 활용하여 문제 1~4를 해결하시오.
"""
students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]

"""
문제 1: 각 학생의 평균 점수를 계산하여 딕셔너리로 반환하는 함수
"""
"""
    1. 각 학생의 평균 점수를 계산하여 딕셔너리로 반환하는 함수
    
    Args:
        students (list): 학생 정보가 담긴 리스트
    
    Returns:
        dict: {학생이름: 평균점수} 형태의 딕셔너리
"""

def calculate_student_averages(students:list) -> dict:
    return [
        {
            "name":s["name"],
            "average":sum(s["subjects"].values())/len(students)
        }
        for s in students
    ]

"""
    2. 특정 과목의 전체 학생 평균을 계산하는 함수
    
    Args:
        students (list): 학생 정보가 담긴 리스트
        subject_name (str): 평균을 구할 과목명
    
    Returns:
        float: 해당 과목의 전체 학생 평균점수
"""
def calculate_subject_average(students:list, subject_name:str) -> float:

    return sum([x["subjects"][subject_name] for x in students])/len(students)

"""
문제 3: 가장 높은 평균 점수를 가진 학생을 찾는 함수
"""
"""
    3. 가장 높은 평균 점수를 가진 학생을 찾는 함수
    
    Args:
        students (list): 학생 정보가 담긴 리스트
    
    Returns:
        dict: {"name": 학생이름, "average": 평균점수} 형태의 딕셔너리
"""
def find_top_student(students:list) -> dict:
    averages= calculate_student_averages(students)
    max_average = 0
    name=""
    for x in averages:
        if max_average < x["average"]:
            max_average= x["average"]
            name = x["name"]

    return {"name": name, "average": max_average}


"""
문제 4: 모든 과목에서 80점 이상인 학생들의 이름을 리스트로 반환하는 함수
"""
"""
    4. 모든 과목에서 80점 이상인 학생들의 이름을 리스트로 반환하는 함수
    
    Args:
        students (list): 학생 정보가 담긴 리스트
        threshold (int): 기준 점수 (기본값: 80)
    
    Returns:
        list: 모든 과목에서 기준점수 이상인 학생들의 이름 리스트
"""
def find_excellent_students(students:list, threshold:int=80) -> list:
    results=[""]
    for s in students:
        if all( a >= threshold for a in s["subjects"].values()):
            results.append({"name": s["name"]})

    return results


print(calculate_student_averages(students))
print(calculate_subject_average(students, "수학"))
print(find_top_student(students))
print(find_excellent_students(students, 80))