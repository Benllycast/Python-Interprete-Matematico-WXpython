
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "BENJAMIN"
__date__ = "$17/05/2011 08:54:46 PM$"

import math

from Stack import Stack
import random

class Parseador():
    def __init__(self):
        self.ultimaParseada = 0

    def parsear(self, exprecion):
        # @type exprecion: unicode
	# @type expr: unicode
	# @type fragmento: unicode
	# @type cont: int
	# @type funciones: tuple

	pilaNumeros = Stack("numeros")
        pilaOperadores = Stack("operadores");
        expr = exprecion.lower()
        aux = expr.strip()        
        expr = aux        
        fragmento = u""
        pos = 0; tamano = 0
        cont = 0;
        funciones = [u"1 2 3 4 5 6 7 8 9 0 ( ) x e + - * / ^ %",
            u"pi",
            u"ln",
            u"log( abs( sen( cos( tan( sec( csc( cot( sgn(",
            u"rnd() asen( asin( acos( atan( asec( acsc( acot( senh( sinh( coh( tanh( sech( csch( coth( sqrt(",
            u"round( asenh( acosh( atanh( asech( acsch( acoth("]
        parentesis = u"( ln log abs sen sin cos tan sec csc cot sgn asen asin acos atan asec acsc acot senh sinh cosh tanh sech csch coth sqrt round asenh asinh acosh atanh asech acsch acoth"
        anterior = -1
        try:
            while pos < len(expr):
                tamano = 0
                cont = 1
                while tamano == 0 and cont <= 6:
                    if (pos + cont <= len(expr)) and funciones[cont-1].find(expr[pos: pos + cont]) != -1:
                        tamano = cont                        
                    cont = cont + 1

                if tamano == 0:
                    self.ultimaParseada = u"0"
                    print "error en la exprecion tamano == 0"
                    raise ArithmeticError, "Error en la exprecion"
                
                elif tamano == 1:

                    if expr[pos: pos + tamano].isnumeric():
                        if anterior == 1 or anterior == 4:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")
                            
                        fragmento = u""
                        while True:
                            fragmento = fragmento + expr[pos]
                            pos += 1
                            if pos >= len(expr) or (not expr[pos:pos + tamano].isnumeric()) or (not expr[pos] == u'.'):
                                break
                                
                        try:
                            float(fragmento)
                        except ValueError:
                            self.ultimaParseada = 0
                            raise NotANumber, "Numero mal digitado"

                        pilaNumeros.push(fragmento)
                        anterior = 1
                        pos -= 1

                    elif expr[pos] == u'x' or expr[pos] == u'e':
                        if anterior == 1 or anterior == 4:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")
                            
                        pilaNumeros.push(expr[pos:pos + tamano])
                        anterior = 1

                    elif expr[pos] == u"+" or expr[pos] == u"*" or expr[pos] == u"/" or expr[pos] == u"%":
                        if anterior == 0 or anterior == 2 or anterior == 3:
                            raise ArithmeticError, 'error en la exprecion'

                        self.sacaOperadores(pilaNumeros, pilaOperadores, expr[pos:pos + tamano])
                        anterior = 2

                    elif expr[pos] == u'^':
                        if anterior == 0 or anterior == 2 or anterior == 3:
                            raise ArithmeticError, 'Error en la exprecion'

                        pilaOperadores.push(u"^")
                        anterior = 2

                    elif expr[pos] == u'-':
                        if anterior == 0 or anterior == 2 or anterior == 3:
                            pilaNumeros.push(u"-1")
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")
                        else:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"-")

                        anterior = 2

                    elif expr[pos] == u"(":
                        if anterior == 1 or anterior == 4:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")

                        pilaOperadores.push(u"(")
                        anterior = 3

                    elif expr[pos] == u")":
                        if anterior != 1 and anterior != 4:
                            raise ArithmeticError, 'error en la exprecion'

                        while (not pilaOperadores.isEmpty()) and parentesis.find(pilaOperadores.peek()) == -1:
                            self.sacaOperador(pilaNumeros, pilaOperadores)

                        if not (pilaOperadores.peek() == u"("):
                            pilaNumeros.push(pilaNumeros.pop() + u" " + pilaOperadores.pop())
                        else:
                            pilaOperadores.pop()

                        anterior = 4

                elif tamano >= 2:
                    fragmento = expr[pos: pos + tamano]

                    if fragmento == u"pi":
                        if anterior == 1 or anterior == 4:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")

                        pilaNumeros.push(fragmento)
                        anterior == 1

                    elif fragmento == u"rnd()":
                        if anterior == 1 or anterior == 4:
                            sacaOperadores(pilaNumeros, pilaOperadores, u"*")

                        pilaNumeros.push(u"rnd")
                        anterior = 1

                    else:
                        if anterior == 1 or anterior == 4:
                            self.sacaOperadores(pilaNumeros, pilaOperadores, u"*")

                        pilaOperadores.push(fragmento[0:len(fragmento)-1])
                        anterior = 3

                pos += tamano

            while not pilaOperadores.isEmpty():
                if parentesis.find(pilaOperadores.peek()) != -1:
                    raise ArithmeticError, 'hay un parentesis de mas'

                self.sacaOperador(pilaNumeros, pilaOperadores)

        except ArithmeticError:
            ultimaParseada = u"0";
            raise ArithmeticError, "Exprecion Mal digitadad"

	print pilaNumeros.len()
        ultimaParseada = pilaNumeros.pop()

        if not pilaNumeros.isEmpty():
            ultimaParseada = u"0"
            raise ArithmeticError, 'Error en la exprecion'
        
        return ultimaParseada


    def fEvaluar(self, exprecionParceada, x):
        """
        funcion que evalua la exprecion ya parseada
        exprecionParceada: unicode
        x: nuemro
        """
        # @type pilaEvaluar: Stack
        # @type exprecionParceada unicode
        #tokenActual = u""
        pilaEvaluar = Stack()
        a = 0; b = 0        
        tokens = exprecionParceada.split();
        
        try:
            for tok in tokens:
                if tok == u"e":
                    pilaEvaluar.push(math.e)
                elif tok == u"pi":
                    pilaEvaluar.push(math.pi)
                elif tok == u"x":
                    pilaEvaluar.push(float(x))
                elif tok == u"+":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a + b))
                elif tok == u"-":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a-b))
                elif tok == u"*":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a * b))
                elif tok == u"/":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a / b))
                elif tok == u"^":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a ** b))
                elif tok == u"%":
                    a = float(pilaEvaluar.pop())
                    b = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(a % b))
                elif tok == u"ln":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.log1p(a))
                elif tok == u"log":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.log10(a))
                elif tok == u"abs":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.fabs(a))
                elif tok == u"rnd":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(random.random())
                elif tok == u"sen" or tok == u"sin":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.sin(a))
                elif tok == u"cos":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.cos(a))
                elif tok == u"tan":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(math.tan(a))
                elif tok == u"sec":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.cos(a)))
                elif tok == u"csc":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.sin(a)))
                elif tok == u"cot":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.tan(a)))
                elif tok == u"sgn":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(self.sgn(a)))
                elif tok == u"asen" or tok == u"asin":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.asin(a)))
                elif tok == u"acos":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.acos(a)))
                elif tok == u"atan":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.atan(a)))
                elif tok == u"asec":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.acos(1 / a)))
                elif tok == u"acsc":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.asin(1 / a)))
                elif tok == u"acot":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.atan(1 / a)))
                elif tok == u"senh" or tok == u"sinh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.sinh(a)))
                elif tok == u"cosh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.cosh(a)))
                elif tok == u"tanh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.tanh(a)))
                elif tok == u"sech":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.cosh(a)))
                elif tok == u"csch":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.sinh(a)))
                elif tok == u"coth":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.tanh(a)))
                elif tok == u"asenh" or tok == u"asinh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.asinh(a)))
                elif tok == u"acosh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.acosh(a)))
                elif tok == u"atanh":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.atanh(a)))
                elif tok == u"asech":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.acosh(a)))
                elif tok == u"acsch":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.asenh(a)))
                elif tok == u"acoth":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(1 / math.atanh(a)))
                elif tok == u"sqrt":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(math.sqrt(a)))
                elif tok == u"round":
                    a = float(pilaEvaluar.pop())
                    pilaEvaluar.push(float(round(a)))
                else:
                    pilaEvaluar.push(float(tok))
        except ArithmeticError:
            print "Exprecion mal parceada"
        a = float(pilaEvaluar.pop())
        if not pilaEvaluar.isEmpty():
            raise ArithmeticError, "exprecion mal digitada"
        return a

    def f(self, x):
        try:
            return self.fEvaluar(exprecionParceada, x)
        except ArithmeticError:
            raise ArithmeticError, "exprecion mal digitada"


    def sacaOperadores(self, pilaNumeros, pilaOperadores, simbolo):
        #@type pilaNumeros: Stack
        #@type pilaOperadores: Stack
        parentesis = u"( ln log abs sen sin cos tan sec csc cot sgn asen asin acos atan asec acsc acot senh sinh cosh tanh sech csch coth sqrt round asenh asinh acosh atanh asech acsch acoth"
        while (not pilaOperadores.isEmpty()) and (parentesis.find(pilaOperadores.peek()) == -1) and (len(pilaOperadores.peek()) == 1) and (self.prioridad((pilaOperadores.peek())[0]) >= self.prioridad(simbolo[0])):
            self.sacaOperador(pilaNumeros, pilaOperadores)

        pilaOperadores.push(simbolo)

   
    def sacaOperador(self, pilaNumeros, pilaOperadores):
        #@type pilaNumeros: Stack
        #@type pilaOperadores: Stack
        operador = u""; a = u""; b = u""
        operadoresBinarios = u"+ - * / ^ %"
        try:
            operador = pilaOperadores.pop()
            if operadoresBinarios.find(operador) != -1:
                a = pilaNumeros.pop()
                b = pilaNumeros.pop()
                pilaNumeros.push(a + u" " + b + u" " + opareador)
            else:
                a = pilaNumeros.pop()
                pilaNumeros.push(a + u" " + operador)
        except:
            print "exepcion en sacaOperador"

    def prioridad(self, s):
        if s == u'+' or s == u'-':
            return 0
        elif s == u'*' or s == u'/' or s == u'%':
            return 1
        elif s == u'^':
            return 2
        return -1

    def isNum(self, s=u""):
        pass

    
    # @type polinomio: unicode
    def quitarEspacios(self, polinomio):
        cadeanaSinEspacio = u""
        for i in polinomio:
            if i != r"\s":
                cadeanaSinEspacio = cadeanaSinEspacio + i
        return cadeanaSinEspacio
   

    def sgn(self, numero):
        if numero < 0:
            return -1
        elif numero > 0:
            return 1
        else:
            return 0

