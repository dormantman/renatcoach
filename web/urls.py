from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index view'),
    path('mail/', views.MailView.as_view(), name='Mail view'),
]
