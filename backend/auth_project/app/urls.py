from django.urls import path
from .views import RegisterView, LoginView, LogoutView, DashboardView, ApproveUserView, unapproved_users

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('approve/<int:user_id>/', ApproveUserView.as_view(), name='approve-user'),
    path('users/', unapproved_users, name='unapproved-users'),
]
