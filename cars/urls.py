from django.urls import path
from cars.views import *
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    #pk primary key соответствующей записи в бд.
    path('car/detail/<int:pk>/', CarDetailView.as_view())
]