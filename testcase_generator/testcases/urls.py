from django.urls import path

from . import views

app_name = 'testcases'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:testcase_id>/', views.testcase_detail, name='testcase_detail'),
    path('create/', views.create_testcase, name='testcase_create'),
    path('edit/<int:testcase_id>/', views.edit_testcase, name='testcase_edit'),
]
