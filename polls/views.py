from django.shortcuts import render

from django.http import HttpResponse

# 장고에서의 views는 요청을 처리하는 함수들의 집합. 엔드포인트에 대한 요청을 처리하는 함수들을 작성하는 곳.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
