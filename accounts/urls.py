from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('login/', views.user_login, name='login'),
   # path('logout/', views.logout_view, name='logout'),
]
