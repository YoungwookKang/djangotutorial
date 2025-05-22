from django.urls import path # path 함수는 URL 패턴과 뷰 함수를 매핑하는 데 사용됩니다.

from . import views # 현재 디렉토리(polls 앱)의 views.py 모듈을 가져옵니다. 여기에는 우리가 정의한 뷰 함수들이 있습니다.

# app_name 변수는 URL 네임스페이스(namespace)를 설정합니다.
# 이렇게 하면 다른 앱에서 동일한 URL 이름을 사용하더라도 구분할 수 있습니다.
# 예를 들어, 템플릿에서 {% url 'polls:detail' question.id %} 와 같이 사용합니다.
app_name = "polls"

# urlpatterns 리스트는 이 앱(polls) 내의 URL 패턴들을 정의합니다.
# Django는 요청된 URL과 이 패턴들을 순서대로 비교하여 일치하는 것을 찾습니다.
urlpatterns = [
  # ex: /polls/ (이 앱의 기본 URL)
    # 첫 번째 인자: URL 패턴 문자열. 빈 문자열은 /polls/ 자체를 의미합니다 (mysite.urls에서 /polls/로 시작하는 요청이 이리로 오기 때문).
    # 두 번째 인자: 이 URL 패턴과 일치할 때 호출될 뷰 함수 (views.py의 index 함수).
    # name 인자: 이 URL 패턴에 이름을 부여합니다. 템플릿이나 코드에서 URL을 하드코딩하는 대신 이 이름을 사용할 수 있어 유연성이 높아집니다.
    path("", views.index, name="index"),
    
    # ex: /polls/5/ (숫자 ID를 가진 질문 상세 페이지)
    # "<int:question_id>/": URL 경로의 일부를 캡처하여 뷰 함수에 인자로 전달합니다.
    #   - int: 경로 변환기(path converter)로, 이 부분이 정수여야 함을 의미합니다.
    #   - question_id: 캡처된 값에 대한 변수 이름. views.detail 함수의 question_id 매개변수로 전달됩니다.
    path("<int:question_id>/", views.detail, name="detail"),
    
    # ex: /polls/5/results/ (특정 질문의 결과 페이지)
    path("<int:question_id>/results/", views.results, name="results"),
    
    # ex: /polls/5/vote/ (특정 질문에 대한 투표 처리 URL)
    path("<int:question_id>/vote/", views.vote, name="vote"),
]