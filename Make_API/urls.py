from django.urls import path
from . import views
from Make_API.views import login_redirect
from django.contrib.auth import login, authenticate
urlpatterns = [
    path('', login_redirect, name='login_redirect'),
    path('home/', views.home_page, name='homepage'),
    path('create-instance', views.create_instance, name='create_instance'),
    path('profile/', views.view_profile, name='view_profile'),
    path('home/profile/edit', views.edit_profile, name='edit_profile'),
    path('register', views.register, name='register'),
    path('clientarea/registration/', views.register, name="user_registration",),
    # path('login/',views.UserLogin.as_view(), name='login'),
    path('login/', views.login_request, name='login'),
    # path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('logout/', views.logout_request, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path("password_reset", views.password_reset_request, name="password_reset"),
]