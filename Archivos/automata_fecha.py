class analizar_fecha:
    def __init__(self):
        self.letra_actual = ''
        self.estado_actual = 0
        self.valor_lexema = ''
        self.operadores = ['-','\\']
        self.aceptacion = True
        self.aresultado = ''

    def switch(self, estado):
        self.estados = {
            0: self.estado_cero,
            1: self.estado_uno,
            2: self.estado_dos,
            3: self.estado_tres,
            4: self.estado_cuatro,
            5: self.estado_cinco,
            6: self.estado_seis,
            7: self.estado_siete,
            8: self.estado_ocho,
            9: self.estado_nueve,
            10: self.estado_diez,
            11: self.estado_once,
            12: self.estado_doce,
            13: self.estado_trece,
            14: self.estado_catorce,
        }

        func = self.estados.get(estado, lambda: 'No es un caracter válido')
        return func()

    def valuar_dato(self, dato):
        try:
            int(dato)
            return True
        except ValueError:
            return False

    def estado_cero(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 0:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 1:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 2:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) > 2 :
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_uno(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) <= 9:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_dos(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) in self.operadores:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_tres(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10: 
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_cuatro(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) in self.operadores:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')        

    def estado_cinco(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 0:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 1:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')     
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')           

    def estado_seis(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10: 
                self.estado_actual = 7
                self.valor_lexema = self.valor_lexema + self.letra_actual 
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_siete(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) in self.operadores:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')   

    def estado_ocho(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 0:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif 0 < int(self.letra_actual) < 3:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print('cadena no aceptada')
        else:
            self.aceptacion = False
            print('cadena no aceptada')            

    def estado_nueve(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) in self.operadores:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')        

    def estado_diez(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10: 
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')  

    def estado_once(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10:
                self.estado_actual = 12
                self.valor_lexema = self.valor_lexema + self.letra_actual
                self.aresultado = str('<span class ="fecha">'+ self.valor_lexema + '</span>'+' ')
            elif  int(self.letra_actual) == 0 :
                self.estado_actual = 12
                self.valor_lexema = self.valor_lexema + self.letra_actual
                self.aresultado = str('<span class ="fecha">'+ self.valor_lexema + '</span>'+' ')
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_doce(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10:
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif  int(self.letra_actual) == 0 :
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_trece(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif  int(self.letra_actual) == 0 :
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')
    
    def estado_catorce(self):
        if self.valuar_dato(self.letra_actual) == True:
            if 0 < int(self.letra_actual) < 10:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
                self.aresultado = str('<span class ="fecha">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = True
            elif int(self.letra_actual) == 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
                self.aresultado = str('<span class ="fecha">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = True
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def analizar(self, cadena):
        cadena = str(cadena)
        palabras = cadena.split()
        for i in palabras:
            self.aceptacion = True
            self.valor_lexema = ""
            self.estado_acutal = 0
            i = i + ' '
            for x in i:
                if self.aceptacion == True:
                    self.letra_actual = x
                    self.switch(self.estado_actual)
            print(self.aresultado)
            return self.aresultado

#analizar_fecha().analizar(input('Escriba la cadena: '))