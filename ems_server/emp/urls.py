from django.urls import path

from emp import views

urlpatterns = [
    path("employees/", views.EmployeeAPIView.as_view()),
    path("employees/<str:pk>/", views.EmployeeAPIView.as_view()),
]
