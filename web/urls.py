from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index view'),
    path('mail/', views.MailView.as_view(), name='Mail view'),
    path('emails/', views.EmailsView.as_view(), name='Emails view'),
    path('login/', views.LoginView.as_view(), name='Login view'),
    path('logout/', views.LogoutView.as_view(), name='Logout view'),
]
