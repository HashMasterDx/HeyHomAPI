from django.urls import path
from .views import *


urlpatterns = [
    path('', ApiOverview, name='home'),
    path('create/', create_property, name='create'),
    path('list/', list_property, name='list'),
    path('detail/<str:pk>/', detail_property, name='detail'),
    path('update/<str:pk>/', update_property, name='update'),
    path('delete/<str:pk>/', delete_property, name='delete'),
]
