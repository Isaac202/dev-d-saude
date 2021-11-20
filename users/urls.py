from django.urls import path
from .views import create_user_adm,login_user,logout_user,usuario,edit_user_admin,edit_user,delete_user

urlpatterns = [
    path('user_adm_add/',create_user_adm, name='user_adm'),
    path('login_user/',login_user, name='login'),
    path('logout_user/',logout_user, name='logout'),
    path('usuario/',usuario, name='usuario'),
    path('edit_user_admin/',edit_user_admin, name='edit_user_admin'),
    path('edit_user/',edit_user, name='edit_user'),  
    path('delete_user/',delete_user, name='delete_user'),  
    
]