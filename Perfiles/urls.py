from django.contrib import admin
from django.urls import path
from Perfiles.views import registro, SignInView, SignOutView, view_profile, activate, edit_profile, login_email, UserListView

urlpatterns = [
    path('', SignInView.as_view(), name='inicio'),
    path('registro/', registro, name='sign_up' ),
    path('iniciar-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    path('Inicio/', login_email,  name='bienvenida'),
    path('usuarios/', UserListView.as_view(), name='usuarios' ),
    path('perfil/', view_profile,  name='perfil'),
    path('activate/<uidb64>[0-9A-Za-z_\-]+)/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
    path('editar/', edit_profile, name='editar' ),
]
