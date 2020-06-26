from django.urls import path,include
from userapp import views

# Template Tagging
app_name = 'userapp'

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/', views.user_login, name = 'user_login'),
]
