class analizar_texto:
    def __init__(self):
        self.letra_actual = ''
        self.estado_actual = 0
        self.valor_lexema = ''
        self.operadores = ['+','-','*','x','.','^','/','-']
        self.punt = [',',':',';','.',')','(']
        self.aceptacion = True
        self.reserv = ['teorema','Teorema','Matemático','matemático','Matemática','matemática',
        'Hilbert','Turing','Análisis','análisis','Euler','Fermat','Pitágoras','Autómata','autómata','Boole',
        'Cantor','Perelman','Experimentación','experimentación','Físico','físico','Física','física',
        'Astronomía','astronomía','Mecánica','mecánica','Newton','Einstein','Galileo','Modelo','modelo',
        'Tesla','Dinámica','dinámica','Partículas','partículas', 'Hugo']
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
            15: self.estado_quince,
            16: self.estado_dieciseis,
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
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) in self.punt:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
    
    def estado_uno(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_dos(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[4]:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[2] or str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                #print( 'Esto es un número entero ', self.valor_lexema)
                self.aceptacion = False
                self.aresultado = str('<span class ="entero">'+ self.valor_lexema + '</span>'+' ')
            elif str(self.letra_actual) == '-':
                #print( 'Esto es un número entero ', self.valor_lexema)
                self.aceptacion = False
                self.aresultado = str('<span class ="entero">'+ self.valor_lexema + '</span>'+' ')
            elif str(self.letra_actual) in self.punt:
                #print( 'Esto es un número entero ', self.valor_lexema)
                self.aceptacion = False
                self.aresultado = str('<span class ="entero">'+ self.valor_lexema + '</span>'+' ')
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 2
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True
        
    def estado_tres(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_cuatro(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 1:
                self.estado_actual = 7
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def estado_cinco(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >=0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_seis(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[2] or str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
               # print( 'Esto es un número real ', self.valor_lexema)
                self.aresultado = str('<span class ="real">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                #print( 'Esto es un número real ', self.valor_lexema)
                self.aresultado = str('<span class ="real">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 6
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True
    
    def estado_siete(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 0:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def estado_ocho(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[4]:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 8
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_nueve(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[5]:
                self.estado_actual = 12
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual   
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')

    def estado_diez(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_once(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
               # print( 'Esto es un número complejo ',self.valor_lexema)
                self.aresultado = str('<span class ="complejo">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
               # print( 'Esto es un número complejo ', self.valor_lexema)
                self.aresultado = str('<span class ="complejo">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print( 'Cadena no aceptada')
    
    def estado_doce(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self. letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            if str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 15
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def estado_trece(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            if str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def estado_catorce(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            if str(self.letra_actual) == ' ':
              #  print( 'Número en notación científica ', self.valor_lexema)
                self.aresultado = str('<span class ="notacion">'+ self.valor_lexema + '</span>'+ ' ')
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
              #  print( 'Número en notación científica ', self.valor_lexema)
                self.aresultado = str('<span class ="notacion">'+ self.valor_lexema + '</span>'+' ')
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
            
    def estado_quince(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print( 'Cadena no aceptada')
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_dieciseis(self):
        if str(self.letra_actual) == ' ':
            if self.valor_lexema in self.reserv:
               # print( 'Esto es una palabra reservada ', self.valor_lexema)
                self.aresultado = str('<span class ="reservada">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
               # print( 'Esto es unacadena ', self.valor_lexema)
                self.aresultado = str('<span class ="palabra">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            else:
              #  print( 'Esto es una cadena ', self.valor_lexema)
                self.aresultado = str('<span class ="palabra">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
        elif str(self.letra_actual) in self.punt:
            if self.valor_lexema in self.reserv:
               # print( 'Esto es una palabra reservada ', self.valor_lexema)
                self.aresultado = str('<span class ="reservada">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
               # print( 'Esto es unacadena ', self.valor_lexema)
                self.aresultado = str('<span class ="palabra">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
            else:
              #  print( 'Esto es una cadena ', self.valor_lexema)
                self.aresultado = str('<span class ="palabra">'+ self.valor_lexema + '</span>'+' ')
                self.aceptacion = False
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual 
            self.aceptacion = True

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


#analizar_texto().analizar(input('Escriba la cadena: '))

