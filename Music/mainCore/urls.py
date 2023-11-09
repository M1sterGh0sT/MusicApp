from django.urls import path

from . import views



app_name = 'core'


urlpatterns = [
    path('name/', views.index, name='page1'),
    path('index2/', views.index2, name='page2'),
]


