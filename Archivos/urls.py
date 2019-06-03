from django.contrib import admin
from django.urls import path
from Archivos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('subida_archivos/', subida_archivos, name='subida_archivos'),
    path('archivos_subidos/', lista_archivos, name='archivos_subidos'),
    path('ver_archivo/', ver_archivo, name='leer'),
    path('ver_editado/', guardar, name='guardar' ),
    path('analizar/', analizar_archivo, name='analizar' ),
    path('archivos/', ArchivosView.as_view(), name='archivos'),
    path('expresión_regular/', ExpresionView, name='regex' ),
    path('automata/', AutomataView.as_view(), name='automata'),
    path('ver_analizado/', analizar_automata, name='analizado'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)