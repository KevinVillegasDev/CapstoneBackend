from django.urls import path
from measurements import views


urlpatterns = [
    path('measurements', views.MeasurementList.as_view()),
    
]