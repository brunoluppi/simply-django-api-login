from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.user_register),
    path('login/', views.user_login),
    path('validatetoken/', views.validate_token),
    path('modifyuser/', views.modify_user),
    path('forgotpassword/', views.forgot_password),
    path('deleteaccount/', views.delete_account)
]
