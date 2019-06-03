from django import forms
from Archivos.models import  Documento, Expresion

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ("archivo",)
       
class ExpresionForm(forms.ModelForm):
    class Meta:
        model = Expresion
        fields = ("expresion",)