# myapp/views.py

from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("안녕하세요, Django 웹 서버입니다!")

# 새로운 뷰 함수 추가
def show_env_vars(request):
    # os.getenv를 사용하여 환경 변수들을 가져옵니다.
    site_name = os.getenv('SITE_NAME')

    # HTML 형식으로 응답을 구성합니다.
    html_response = f"""
    <h1>.env 파일에 정의된 환경 변수</h1>
    <p><strong>SITE_NAME:</strong> {site_name}</p>
    """

    return HttpResponse(html_response)