from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_lesson/<str:pk>', views.updateLesson, name='update_lesson'),
    path('delete/<str:pk>', views.deleteLesson, name='delete'),
]
