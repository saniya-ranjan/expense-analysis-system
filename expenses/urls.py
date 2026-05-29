from django.urls import path
from . import views
from .views import register
from .views import user_login, user_logout

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name="add_expense"),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]