def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.p2']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'La extensión no es válida')


def validar_expresion(expresion):
        from Archivos.regex import regexAafnd
        from django.core.exceptions import ValidationError
        regex = regexAafnd(expresion).construirAFND()
        if expresion == " ":
                raise ValidationError(u' ')
        elif regex == False:
                raise ValidationError(u'Expresión inválida')
         
