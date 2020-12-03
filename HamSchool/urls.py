"""HamSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from HamSchool.Apps.vistas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/', auth_views.LoginView.as_view()),
    path('login', auth_views.LoginView.as_view()),
    path('reset_password/login', auth_views.LoginView.as_view()),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="vistas/Login/olvp.html"), name="reser_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_comlete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    path('logout', views.logout_requesr, name="logout"),

    

    path('register', views.register_request, name="register"),
    path('reset_password/register', views.register_request, name="register"),

    
    path('accounts/login', views.login_request, name="login"),
    path('index', views.index_request, name="index"),
    path('cursos', views.Curso_curos, name="cursos"),
    path('about_us', views.about_us, name="about us"),
    path('olvp', views.olvp, name="RecuperarContraeña"),
  

    path('Kinder', views.curso_kinder, name="Curso kinder"),
    path('KinderNum', views.curso_kinder_num, name="Curso Kinder numeros"),
    path('KinderAbc', views.curso_kinder_abc, name="curso Kinder Abc"),
    path('KinderAnim', views.curso_kinder_anim, name="curso Kinder Anim"),
    path('KinderCol', views.curso_kinder_Col, name="curso Kinder Col"),
    path('KinderFinal', views.curso_kinder_Final, name="curso Kinder Final"),


    path('Primaria', views.curso_Primaria, name="Curso primaria"),
    path('PrimariaAbc', views.curso_Primaria_Abc, name="Cursos Primaria abc"),
    path('Primarianum', views.curso_Primaria_Num, name="Curso Primaria num"),
    path('Primcol', views.curso_Primaria_col, name="Curso Primaria col"),
    path('Primgeo', views.curso_Primaria_geo, name="Curso Primaria geo"),
    path('Primpc', views.curso_Primaria_PC, name="Curso Primaria PC"),
    path('Primpron', views.curso_Primaria_pron, name="Curso Primaria pron"),
    path('PrimFinal', views.curso_Primaria_Final, name="Curso Primaria Final"),


    path('Secu', views.cursos_sec, name="Curso sec"),
    path('SecToBe', views.cursos_sec_Tobe, name="Curso Tobe"),
    path('SecPC', views.cursos_sec_pc, name="Cursos PC"),
    path('SecNum', views.cursos_sec_num, name="Cursos Num"),
    path('SecFam', views.cursos_sec_fam, name="Cursos Fam"),
    path('Secabc', views.cursos_sec_acb, name= "Cursos abc"),
    path('Sectiempo', views.cursos_sec_tiempo, name="Cursos tiempo"),
    path('SecFinal', views.cursos_sec_final, name="Cursos final"),


    path('memorama', views.games_memorama, name="Game memorama"),
    path('ahorcado', views.games_ahorcado, name="Game ahorcado"),
    path('sopadeletras', views.games_letras, name="Game letras"), 


    path('paypalk', views.paypalk, name="paypalkinder"),
    path('paypals', views.paypals, name="paypalprimaria"),
    path('paypalp', views.paypalp, name="paypalsecundaria"),

    path('lista', views.lista_usuarios, name="lista"),

]

urlpatterns += staticfiles_urlpatterns()