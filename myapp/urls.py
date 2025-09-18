# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('env/', views.show_env_vars, name='show_env'), # 새로운 엔드포인트 추가
]