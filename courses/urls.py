from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category-list', views.categories, name="categories"),
    path('category/<int:pk>/', views.category, name="category"),
    path('course/<int:pk>/', views.course, name='course'),
    path('courses/', views.courses, name="courses")
]
