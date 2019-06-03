from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView 
from Perfiles.forms import RegistroForm, UserForm, EditProfileForm, EditUserForm
from Perfiles.models import Perfil 
from Perfiles.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.

class SignInView(LoginView):
    template_name = 'iniciar_sesion.html'

@transaction.atomic
def registro(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = RegistroForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            nuevo_usuario = form1.save()
            nuevo_usuario.refresh_from_db()
            extra_usuario = RegistroForm(request.POST, instance=nuevo_usuario.perfil)
            extra_usuario.full_clean()
            extra_usuario.save(commit=False)
            extra_usuario.is_active = False
            extra_usuario.save()
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta'
            message = render_to_string('activacion.html', {
                'user': nuevo_usuario,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(nuevo_usuario.pk)),
                'token':account_activation_token.make_token(nuevo_usuario),
            })
            to_email = form1.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'confirmar.html')
    else:
        form1 = UserForm()
        form2 = RegistroForm()
    return render(request, 'registro.html', {'form1': form1, 'form2': form2})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'gracias.html')
    else:
        return HttpResponse('Activation link is invalid!')

        
@login_required
def login_email(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'usuario': user, 'username' : user.username}
    login_ip = request.META['REMOTE_ADDR']  
    mail_subject = 'Inicio de sesión'
    message = render_to_string('correo_login.html', {
            'user': user,
            'login':user.last_login,
            'ip' : login_ip,
            })
    to_email = user.email
    email = EmailMessage( mail_subject, message, to=[to_email])
    email.send()
    return render(request, 'bienvenida.html', args)


@login_required
def view_profile(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    args = {'usuario': user, 'username' : user.username}
    return render(request, 'profile.html', args)

def edit_profile(request):
    content = {}
    profile = request.user.get_username()
    if request.method == 'POST':
        form1 = EditUserForm(request.POST, instance=request.user)
        form2 = EditProfileForm(request.POST, instance=request.user.perfil)
        content['form1'] = form1
        content['form2'] = form2
        if form1.is_valid() and form2.is_valid():
            new_user1 = form1.save()
            new_user2 = form2.save()
            return render(request, 'actualizado.html', content)
    else:
        form1 = EditUserForm(instance=request.user)
        form2 = EditProfileForm(instance=request.user.perfil)
        content['form1'] = form1
        content['form2'] = form2
        return render(request, 'editar.html',content)

class UserListView(ListView):
    model = User
    context_object_name = 'usuarios'
    queryset = User.objects.all()
    template_name = 'lista_usuarios.html'


class SignOutView(LogoutView):
    template_name = 'cerrar_sesion.html'

