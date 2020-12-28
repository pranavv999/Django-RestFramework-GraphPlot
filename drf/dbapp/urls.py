from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('problem1/', views.problem_one_home, name='problem1'),
    path('problem2/', views.problem_two_home, name='problem2'),
    path('problem3/', views.problem_three_home, name='problem3'),
    path('problem4/', views.problem_four_home, name='problem4'),
    path('api/api_list/', views.api_list, name="api-list"),
    path('api/problem_one/', views.problem_one, name='problem1_api'),
    path('api/problem_two/', views.problem_two, name='problem2_api'),
    path('api/problem_three/', views.problem_three, name='problem3_api'),
    path('api/problem_four/', views.problem_fourth, name='problem4_api')
]
