from django.shortcuts import render, get_object_or_404
# from django.template import loader
from django.http import HttpResponse, Http404

from .models import Question, Choice

# 장고에서의 views는 요청을 처리하는 함수들의 집합. 엔드포인트에 대한 요청을 처리하는 함수들을 작성하는 곳.

# index 뷰 함수: /polls/ URL 요청을 처리합니다.
# 가장 최근에 발행된 질문 5개를 가져와서 텍스트로 보여줍니다.
def index(request):
    # Question.objects는 Question 모델의 모든 객체에 접근할 수 있는 매니저(manager)입니다. 각 장고 모델에는 objects라는 매니저가 있음.
    # order_by("-pub_date")는 pub_date 필드를 기준으로 내림차순 정렬합니다 (최신순).
    # [:5]는 정렬된 결과 중 처음 5개만 가져옵니다 (슬라이싱).
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    
    # render 함수는 템플릿을 렌더링하고, 결과를 HttpResponse 객체로 반환합니다.
    # 이 함수는 템플릿 경로와 컨텍스트 데이터를 인자로 받습니다.    
    return render(request, "polls/index.html", context)
# detail 뷰 함수: /polls/<question_id>/ URL 요청을 처리합니다.
# URL에서 question_id 값을 받아서 해당 ID의 질문 내용을 보여줍니다 (현재는 플레이스홀더).
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# results 뷰 함수: /polls/<question_id>/results/ URL 요청을 처리합니다.
# 특정 질문의 결과를 보여줍니다 (현재는 플레이스홀더).
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# vote 뷰 함수: /polls/<question_id>/vote/ URL 요청을 처리합니다.
# 특정 질문의 특정 선택지에 투표하는 기능을 처리합니다 (현재는 플레이스홀더).
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)