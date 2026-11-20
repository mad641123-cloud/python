
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    path('movie/<int:movie_id>/review/', views.add_review, name='add_review'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
