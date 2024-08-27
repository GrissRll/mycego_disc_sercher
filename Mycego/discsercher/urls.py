from django.urls import path
from . import views
urlpatterns = [
    path('', views.take_me_home_cr, name='home'),
    path('folder/', views.show_me_some_thing, name='folder')
]