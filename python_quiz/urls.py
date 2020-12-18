from django.urls import path

from . import views

app_name = "python_quiz"

urlpatterns = [
    path('', views.index, name="index"),
    path('questions/', views.questions, name="questions"),
    path('questions/<int:question_id>/', views.detail, name="detail")
]
