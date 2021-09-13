from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserFunctions.as_view()),
]