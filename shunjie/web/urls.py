from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                                                #首页
    path('jobs/', views.jobs, name='jobs'),                                             #人才招聘
    path('contact/', views.contact, name='contact'),                                    #联系我们
    path('about/', views.about, name='about'),                                          #关于我们
    path('projects/', views.projects, name='projects'),                                 #服务项目
    path('projects/<str:project_name>/', views.projectsdetail, name='projectsdetail'),  #服务项目详情
    path('cases/', views.cases, name='case'),                                           #服务案例
    path('cases/<str:case_name>/', views.casesdetail, name='casedetail'),               #服务案例详情
]