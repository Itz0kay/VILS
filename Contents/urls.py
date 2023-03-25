from django.urls import path
from Contents.views import *

urlpatterns = [
    path('list',contentList, name='contentList'),
    path('detail/<int:pk>',contentdetail, name='contentdetail'),
]