from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog_list/', views.blog_list, name='blogs'),
    path('add_blog/', views.add_blog, name='add_blog'),
]
