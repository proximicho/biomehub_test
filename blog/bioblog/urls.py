from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:post_type>/<str:post_name>', views.details, name='details')
    
]
