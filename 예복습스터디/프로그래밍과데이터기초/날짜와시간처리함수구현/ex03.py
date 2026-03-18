## 주제 5: 날짜와 시간 처리 함수 구현
#Python의 `datetime`, `timedelta`, `calendar` 모듈을 활용하여 다음 5개의 날짜 처리 함수를 구현하세요.

from datetime import datetime
import holidays

brith_date= "1996-03-14"


def validate_date(date_str:str, format="%Y-%m-%d") -> bool:
    """날짜 형식 검증"""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False


def get_weekday_name(index:int) -> str:
    """한국어 요일/월 이름"""
    WEEKDAY_NAMES = ["월", "화", "수", "목", "금", "토", "일"]
    return WEEKDAY_NAMES[index]

def get_holidays_of_2024() -> dict:
    """한국 공휴일 (2024년)"""
    return {
        "2024-01-01": "신정", "2024-03-01": "삼일절", "2024-05-05": "어린이날",
        "2024-06-06": "현충일", "2024-08-15": "광복절", "2024-10-03": "개천절",
        "2024-10-09": "한글날", "2024-12-25": "크리스마스"
    }

    
#[문제1] 나이 계산기
## 문제: 나이 계산기 
#생년월일을 입력받아 현재 나이(만 나이)와 다양한 정보를 출력하는 함수를 작성하세요.

def calculate_age_info(birth_date):
    return {"age": datetime.today()-datetime.strptime(birth_date,"%Y-%m-%d"),"weekday":datetime.weekday(datetime.strptime(birth_date,"%Y-%m-%d")),"lives":(datetime.today()-datetime.strptime(birth_date,"%Y-%m-%d")).days,"birth":True if today.strftime("%m-%d")-datetime.strptime(birth_date,"%Y-%m-%d")[5:] > 0 else False}
    """
    생년월일을 받아 나이 관련 정보를 계산합니다.
    Args:
        birth_date (str): 생년월일 (YYYY-MM-DD 형식)
    
    Returns:
        dict: 나이 정보 딕셔너리
    """

"""
**출력 예시:**
- 만 나이
- 태어난 요일
- 살아온 총 일수
- 올해 생일 통과 유무
"""

#[문제2] 근무일 계산기

## 문제: 근무일 계산기 
#시작일과 종료일을 입력받아 주말과 공휴일을 제외한 실제 근무일을 계산하는 함수를 작성하세요.

def calculate_working_days(start_date, end_date, holidays=None):
    kr_holidays = holidays.KR()
    total_off=0
    total_holiday=0
    total_holi_off=0
    current_date = start_date
    while current_date <= end_date:
        is_week_end = start_date.weekday >=5

        is_holidays= start_date in kr_holidays

        if is_week_end:
            total_off+=1
        if is_holidays:
            total_holiday+=1
        if is_week_end or is_holidays:
            total_holi_off+=1

    return {"총 일수":(datetime.strptime(end_date_str, "%Y-%m-%d")-datetime.strptime(start_date, "%Y-%m-%d")).days,"주말 수":total_off,"공휴일 수":total_holiday,"실제 근무일 (주말 + 공휴일 제외)":end_date.days-start_date.days-(total_holi_off)}
    """
    두 날짜 사이의 근무일(평일)을 계산합니다.
    
    Args:
        start_date (str): 시작일 (YYYY-MM-DD)
        end_date (str): 종료일 (YYYY-MM-DD)
        holidays (list): 공휴일 리스트 (선택사항)
    
    Returns:
        dict: 근무일 관련 정보
    """


# **출력 예시:**
# - 총 일수
# - 주말 수
# - 공휴일 수
# - 실제 근무일 (주말 + 공휴일 제외)

#[문제3] 프로젝트 일정 관리기
## 문제: 프로젝트 일정 관리기
#프로젝트 시작일과 소요 기간(근무일 기준)을 입력받아 완료 예정일을 계산하는 함수를 작성하세요.


def calculate_project_schedule(start_date, duration_days, holidays=None):
    kr_holidays = holidays.KR()
    total_holi_off=0
    current_date = start_date
    while current_date <= (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=duration_days)).strftime("%Y-%m-%d"):
        is_week_end = start_date.weekday >=5

        is_holidays= start_date in kr_holidays

        if is_week_end or is_holidays:
            total_holi_off+=1

    
    return{"프로젝트 완료 예정일":(datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=duration_days)).strftime("%Y-%m-%d"),"소요 근무일":duration_days,"총 달력 일수":(datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=duration_days)-datetime.strptime(start_date, "%Y-%m-%d")).days,"프로젝트 기간 중 공휴일 수":total_holi_off,"마일스톤 날짜들 (25%, 50%, 75% 진행 시점)":(datetime.now()-datetime.strptime(start_str, "%Y-%m-%d")).days /duration_days}

    """
    프로젝트 시작일과 소요 기간으로 완료일을 계산합니다.
    
    Args:
        start_date (str): 프로젝트 시작일
        duration_days (int): 소요 근무일
        holidays (list): 공휴일 리스트
    
    Returns:
        dict: 프로젝트 일정 정보
    """

# **출력 예시:**
# - 프로젝트 완료 예정일
# - 소요 근무일
# - 총 달력 일수
# - 프로젝트 기간 중 공휴일 수
# - 마일스톤 날짜들 (25%, 50%, 75% 진행 시점)

#[문제4] 시간대 변환기
## 문제: 시간대 변환기
#특정 시간대의 날짜/시간을 다른 시간대로 변환하는 함수를 작성하세요.


def convert_timezone_simple(datetime_str, from_timezone, to_timezone):
    
    return {
        "시간 차이": f"{((t := datetime.strptime(datetime_str, '%Y-%m-%d %H:%M').replace(tzinfo=ZoneInfo(from_timezone)).astimezone(ZoneInfo(to_timezone))).utcoffset().total_seconds() - datetime.strptime(datetime_str, '%Y-%m-%d %H:%M').replace(tzinfo=ZoneInfo(from_timezone)).utcoffset().total_seconds()) / 3600:+.1f}시간",
        "원본 시간대 정보": (s := datetime.strptime(datetime_str, '%Y-%m-%d %H:%M').replace(tzinfo=ZoneInfo(from_timezone))).strftime("%Y-%m-%d %H:%M %Z%z"),
        "변환된 시간대 정보": t.strftime("%Y-%m-%d %H:%M %Z%z")
    }
    """
    시간대를 변환합니다.
    
    Args:
        datetime_str (str): 날짜시간 (YYYY-MM-DD HH:MM)
        from_timezone (str): 원본 시간대 (예: 'Asia/Seoul')
        to_timezone (str): 변환할 시간대 (예: 'America/New_York')
    
    Returns:
        dict: 시간대 변환 정보
    """

# **출력 예시:**
# - 시간 차이
# - 원본 시간대 정보
# - 변환된 시간대 정보

