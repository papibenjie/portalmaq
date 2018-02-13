from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>/', views.user_gists),
    path('category/<str:category>/', views.category_gists),
    path('user/<str:username>/category/<str:category>/', views.user_category_gists),
]
