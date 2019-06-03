from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, render_to_response
from Archivos.forms import DocumentoForm, ExpresionForm
from Archivos.models import Documento, user_directory_path
from django.contrib.auth.models import User
from Proyecto import settings
from django.views.generic import ListView
import os
from django.core.files import File
from Archivos.automata import analizar_texto
from Archivos.automata_fecha import analizar_fecha
from Archivos.regex import *

# Create your views here.

def subida_archivos(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Documento(archivo=request.FILES['archivo'],user=request.user.perfil)
            newdoc.save()
            return redirect('archivos_subidos')
    else:
        form = DocumentoForm()
    return render(request, 'subida_archivos.html', {
        'form': form
    })

def lista_archivos(request):
    archivos = Documento.objects.filter(user=request.user.perfil)

    return render(request,'archivos_subidos.html',{'documentos':archivos})

def ver_archivo(request):
    id_ar = request.GET['id_ar']
    documento = Documento.objects.get(id=id_ar).archivo
    documento.open(mode='rb')
    lineas = documento.read()
    print(lineas)
    contenido = lineas.decode('utf-8')
    documento.close()
    return render(request, 'lectura.html', {'id_a':id_ar,'contenido':contenido})

   
def guardar(request):   
    id_archivo = request.POST['id_ar'] 
    print(id_archivo)
    nuevo_contenido = bytes(request.POST['texto'], 'utf-8')
    nuevo = str(request.POST['texto'])
    print(nuevo)
    archivo = Documento.objects.get(id=id_archivo).archivo
    archivo.open(mode='wb')
    archivo.write(nuevo_contenido)
    archivo.close()
    return render(request, 'lectura_guardado.html', {'id_a':id_archivo, 'texto':nuevo})


def analizar_archivo(request):
    parrafo = []
    id_ar = request.POST['id_ar']
    documento = Documento.objects.get(id=id_ar).archivo
    documento.open(mode='rb')
    lineas = documento.readlines()
    print(len(lineas))
    contenidos = []
    for i in range(len(lineas)):
        contenidos.append(lineas[i].decode('utf-8'))
        palabras = contenidos[i].split()
        lista_palabras = []
        for j in palabras:
            resultado1 = analizar_texto().analizar(j)
            if resultado1:
                lista_palabras.append(str(resultado1))
            resultado2 = analizar_fecha().analizar(j)
            if resultado2:    
                lista_palabras.append(str(resultado2))
        parrafo.append( ''.join(lista_palabras)  ) 
        #print(lista_palabras)
    print(parrafo)
    documento.close()
    return render(request, 'analizar.html', {'parrafo':parrafo})


class ArchivosView(ListView):
    model = Documento
    context_object_name = 'archivos'
    queryset = Documento.objects.all()
    template_name = 'lista_archivos.html'

def ExpresionView(request):
    
    if request.method == "POST":
        id_ar = request.POST['id_ar']
        form = ExpresionForm(request.POST)
        if form.is_valid():
            expresion = request.POST.get("expresion")
            print(expresion)
            afndObj = regexAafnd(expresion)
            afnd = afndObj.obtenerAFND()
            afdObj = AFNDaAFD(afnd)
            afd = afdObj.obtenerAFD()
            regex = "Expresion regular: " + expresion
            grafica = dibujarGrafoD(afd, "afd")
            return render(request, "automata.html", {'id_a':id_ar,'expresion': expresion})
    else: 
        id_ar = request.GET['id_ar']
        form = ExpresionForm()
    return render(request, "expresion.html", {'form': form, 'id_a':id_ar})


class AutomataView(TemplateView):
    template_name = 'automata.html'

def analizar_automata(request):
    id_ar = request.GET['id_ar']
    expresion = request.GET.get("expresion")
    afndObj = regexAafnd(expresion)
    afnd = afndObj.obtenerAFND()
    afdObj = AFNDaAFD(afnd)
    afd = afdObj.obtenerAFD()
    documento = Documento.objects.get(id=id_ar).archivo
    documento.open(mode='rb')
    lineas = documento.readlines()
    contenidos = []
    lista_palabras = []
    for i in range(len(lineas)):
        contenidos.append(lineas[i].decode('utf-8'))
        palabras = contenidos[i].split()
        for j in palabras:
            #print("Este es el texto a analizar: ",j)
            resultado1 = analizar_textoA().analizar(afd,j)
           # print("Este es el resultado analizado del texto ",j," :",resultado1)
            if resultado1[j] == 1:
                lista_palabras.append(str(j))
            else:
                pass
    documento.close()
    return render(request, 'analizar_automata.html', {'lista':lista_palabras,'id_ar':id_ar,'expresion':expresion})

