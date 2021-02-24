from django.urls import path, include
from Reminders import views


urlpatterns = [
    path('user/', views.UserAPI.as_view()),
    path('login/', include('rest_framework.urls')),
    path('reminders/', views.ReminderAPI.as_view()),
    path('reminders/<int:pk>/', views.ReminderAPI.as_view()),
    path('notifications/', views.NotificationAPI.as_view()),
    path('notifications/<int:pk>/', views.NotificationAPI.as_view()),
]
