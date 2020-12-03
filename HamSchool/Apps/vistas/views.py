from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomCreationForm 
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

def logout_requesr(request):
    logout(request)
    messages.info(request, "salida exitosa")
    return redirect("vistas/index.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contaseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contaseña)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Usuario o Contraseña invalidad")           
            
    form = AuthenticationForm()
    return render(request, "vistas/login/login.html")



@login_required
def index_request (request):
    return render (request, "vistas/index.html")

def Curso_curos (request):
    return render (request, "vistas/vistafabi1.html")
def about_us (request):
    return render(request,"vistas/about_us.html")
def olvp (request):

    return render (request, "vistas/Login/olvp.html")



def curso_kinder (request):
    return render (request, "vistas/cursos/Kinderindex.html")
def curso_kinder_num (request):
    return render (request, "vistas/cursos/KinderNUm.html")
def curso_kinder_abc (request):
    return render (request, "vistas/cursos/KinderAbc.html")
def curso_kinder_anim (request):
    return render (request, "vistas/cursos/KinderAnim.html")
def curso_kinder_Col (request):
    return render (request, "vistas/cursos/KinderCol.html")
def curso_kinder_Final (request):
    return render (request, "vistas/cursos/KinderFinal.html")

def curso_Primaria (request):
    return render (request, "vistas/cursos/Primindex.html")
def curso_Primaria_Abc (request):
    return render (request, "vistas/cursos/Primabc.html")
def curso_Primaria_Num (request):
    return render (request, "vistas/cursos/Primnum.html")
def curso_Primaria_col (request):
    return render (request, "vistas/cursos/Primcol.html")
def curso_Primaria_geo (request):
    return render (request, "vistas/cursos/Primgeo.html")
def curso_Primaria_PC (request):
    return render (request, "vistas/cursos/PrimPC.html")
def curso_Primaria_pron (request):
    return render (request, "vistas/cursos/Primpron.html")
def curso_Primaria_Final (request):
    return render (request, "vistas/cursos/PrimFinal.html")

def cursos_sec (request):
    return render (request, "vistas/cursos/Secindex.html")
def cursos_sec_pc (request):
    return render (request, "vistas/cursos/SecPC.html")
def cursos_sec_Tobe (request):
    return render (request, "vistas/cursos/SecToBe.html")
def cursos_sec_num (request):
    return render (request, "vistas/cursos/SecNum.html")
def cursos_sec_fam (request):
    return render (request, "vistas/cursos/SecFam.html")
def cursos_sec_acb (request):
    return render (request, "vistas/cursos/Secabc.html")
def cursos_sec_tiempo ( request):
    return render (request, "vistas/cursos/SecTiempo.html")
def cursos_sec_final (request):
    return render (request, "vistas/cursos/SecFinal.html")

def games_memorama(request):
    return render (request, "vistas/memorama.html")
def games_ahorcado (request):
    return render (request, "vistas/cursos/ahorcado.html")
def games_letras (request):
    return render (request, "vistas/sopa-de-letras.html")

def paypalk (request):
    return render (request, "vistas/paypal/paypal.html")
def paypalp (request):
    return render (request, "vistas/paypal/paypalp.html")
def paypals (request):
    return render (request, "vistas/paypal/paypals.html")



def register_request (request):
    data = {
        "form": CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario


    return render(request, "vistas/Login/register.html", data) 


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    
    data = {
            'usuarios': usuarios
    }
    return render(request, "vistas/Lista.html", data)