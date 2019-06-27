from django.urls import path

from apps.mywork import views

urlpatterns = [
    path('salary_check/', views.SalaryCheckPage.as_view(), name='salary_check'),
]
