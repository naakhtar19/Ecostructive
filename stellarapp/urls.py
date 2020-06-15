from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('blog/requestpage/',views.requestpage,name='requestpage'),
    path('requestpage/',views.requestpage,name='requestpage'),
    path('requestpage/success/',views.request_submitted,name='request_submitted'),
]
