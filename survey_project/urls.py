"""
URL configuration for survey_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='survey_app/login.html'), name='login'),
]



# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]


# from django.urls import path
# from survey_app.views import views send_survey_link, fill_survey, approve_survey, user_homepage,survey_submitted,expense_analytics

# urlpatterns = [
#     path('send_survey/', views.send_survey_link, name='send_survey'),
#     path('survey_app/<int:user_id>/', views.fill_survey, name='fill_survey'),
#     path('approve_survey/<int:survey_id>/', views.approve_survey, name='approve_survey'),
#     path('user_home/', views.user_homepage, name='user_home'),
#     path('survey_submitted/', views.survey_submitted, name='survey_submitted'),
#     path('expense_analytics/', views.expense_analytics, name='expense_analytics'),
# ]
from django.urls import path
from survey_app import views

urlpatterns = [
    path('send_survey/', views.send_survey_link, name='send_survey'),
    path('<int:user_id>/fill_survey/', views.fill_survey, name='fill_survey'),
    path('<int:survey_id>/approve/', views.approve_survey, name='approve_survey'),
    path('user_home/', views.user_homepage, name='user_home'),
    path('survey_submitted/', views.survey_submitted, name='survey_submitted'),
    path('analytics/', views.expense_analytics, name='expense_analytics'),
    path('survey_sent/',views.survey_sent,name='survey_sent')
]



