# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class ayudaEvaluador
###########################################################################

class ayudaEvaluador (wx.Dialog):

    def __init__(self, parent):
	wx.Dialog.__init__ (self, parent, id=wx.ID_ANY, title=u"Ayuda", pos=wx.DefaultPosition, size=wx.Size(408, 272), style=wx.DEFAULT_DIALOG_STYLE)

	self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
	self.SetBackgroundColour(wx.Colour(192, 224, 241))

	bSizer5 = wx.BoxSizer(wx.VERTICAL)

	self.txtAyuda = wx.TextCtrl(self, wx.ID_ANY, "Para evaluar una funcion, ingrese la respectiva expresion y precione ENTER\nLa variable permitida es x.\n La expresi�n puede contener las constantes pi y e.\n Los operadores v�lidos de la expresi�n son:\n     OPERACI�N           OPERADOR\n   suma                                 +\n   resta                                  -\n   multiplicaci�n                     *\n   divisi�n                               /\n   potencias                           ^\n   m�dulo                              %\n   par�ntesis                         ( )\n   logaritmo (base e)             ln( )\n   logaritmo (base 10)           log( )\n   valor absoluto                   abs( )\n   n�mero aleatorio               rnd( )\n   seno                                  sen( )\n   coseno                              cos( )\n   tangente                           tan( )\n   secante                             sec( )\n   cosecante                         csc( )\n   cotangente                       cot( )\n   signo                                 sgn( )\n   arcoseno                           asen( )\n   arcocoseno                       acos( )\n   arcotangente                    atan( )\n   arcosecante                      asec( )\n   arcocosecante                  acsc( )\n   arcocotangente                acot( )\n   seno hiperb�lico                senh( )\n   coseno hiperb�lico            cosh( )\n   tangente hiperb�lica         tanh( )\n   secante hiperb�lica           sech( )\n   cosecante hiperb�lica       csch( )\n   cotangente hiperb�lica     coth( )\n   raices cuadradas              sqrt( )\n   arcoseno hiperb�lico        asenh( )\n   arcocoseno hiperb�lico    acosh( )\n   arcotangente hiperb�lica    atanh( )\n   arcosecante hiperb�lica     asech( )\n   arcocosecante hiperb�lica   acsch( )\n   arcocotangente hiperb�lica  acoth( )  \n   redondeo                    round( )\n \n Algunos ejemplos de expresiones v�lidas son:\n x+cos(3)*tan(x^(2*pi*x-1))/acos(1/2)\n cosh(x)+abs(1-x^2)%3", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
	bSizer5.Add(self.txtAyuda, 1, wx.ALL | wx.EXPAND, 5)

	self.SetSizer(bSizer5)
	self.Layout()

	self.Centre(wx.BOTH)

    def __del__(self):
	pass


