from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:testcase_id>/', views.edit_testcase, name='edit'),
    path('list/', views.testcase_list, name='list')
]
