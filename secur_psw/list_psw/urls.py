from django.urls import path
from . import views

app_name = 'password'

urlpatterns = [
    path('',views.list_passwords,name='list_passwords'),
    path('detail/<slug:slug>/',views.password_detail,name='password_detail'),
    path('share/<slug:slug>/',views.password_share,name='share_password'),
    path('create_password/',views.CreatePassword.as_view(),name='create_password'),
]