from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# 모델 클래스는 데이터베이스 테이블에 해당합니다.
# Question 모델은 'polls_question'이라는 테이블로 데이터베이스에 생성됩니다.
class Question(models.Model):
    # CharField는 문자열을 저장하는 필드입니다. max_length는 최대 길이를 지정합니다.
    # 이 필드는 테이블의 'question_text' 컬럼이 됩니다.
    question_text = models.CharField(max_length=200)
    # DateTimeField는 날짜와 시간을 저장하는 필드입니다.
    # "date published"는 관리자 페이지 등에서 이 필드를 설명하는 이름(verbose_name)으로 사용됩니다.
    # 이 필드는 테이블의 'pub_date' 컬럼이 됩니다.
    pub_date = models.DateTimeField("date published")
    
    # __str__ 메소드는 객체를 문자열로 표현할 때 사용됩니다.
    # Django 관리자 사이트나 셸에서 객체를 확인할 때 이 메소드가 반환하는 문자열이 보입니다.
    # f-string을 사용하여 ID와 질문 텍스트를 함께 보여주도록 수정되었습니다.
    def __str__(self):
        return f"{self.question_text}"
    
    # 모델에 정의된 커스텀 메소드입니다.
    # 이 Question 객체가 최근(하루 이내)에 발행되었는지 여부를 True/False로 반환합니다.
    def was_published_recently(self):
        # 현재 시간에서 하루를 뺀 시간보다 발행일이 크거나 같으면 True (즉, 최근 발행)
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice 모델은 'polls_choice'라는 테이블로 데이터베이스에 생성됩니다.
class Choice(models.Model):
    # ForeignKey는 다른 모델과의 관계(일대다 또는 다대일)를 나타냅니다.
    # 여기서는 하나의 Question에 여러 개의 Choice가 속할 수 있음을 의미합니다 (Question이 '일', Choice가 '다').
    # on_delete=models.CASCADE는 연결된 Question 객체가 삭제될 때, 이 Choice 객체도 함께 삭제되도록 설정합니다.
    # 이 필드는 테이블의 'question_id' 컬럼이 되며, polls_question 테이블의 id를 참조합니다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택지 내용을 저장하는 문자열 필드입니다.
    choice_text = models.CharField(max_length=200)
    # 투표 수를 저장하는 정수 필드입니다. default=0은 기본값을 0으로 설정합니다.
    votes = models.IntegerField(default=0)
    
    # Choice 객체를 문자열로 표현할 때 선택지 텍스트를 반환합니다.
    def __str__(self):
        return self.choice_text