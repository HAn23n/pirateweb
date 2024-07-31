from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line
    path('home/<str:user_id>/', views.home, name='home'),
    # path('all_member/', views.all_member, name='all_member'),
    path('random/', views.random_view, name='random'), 
]
