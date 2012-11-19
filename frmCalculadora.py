# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from evaluadorFunciones import EvaFuncion

ID_SALIR = 1000
ID_CALCULADORA_V01_WXPYTHON = 1001
ID_BTN_EXPRESION = 1002
ID_BTN_1 = 1003
ID_BTN_2 = 1004
ID_BTN_3 = 1005
ID_BTN_4 = 1006
ID_BTN_5 = 1007
ID_BTN_6 = 1008
ID_BTN_7 = 1009
ID_BTN_8 = 1010
ID_BTN_9 = 1011
ID_BTN_0 = 1012
ID_BTN_BORRAR = 1013
ID_BTN_SUMA = 1014
ID_BTN_RESTA = 1015
ID_BTN_MULT = 1016
ID_BTN_DIVI = 1017
ID_BTN_CALC = 1018

###########################################################################
## Class frmCalculadora
###########################################################################

class frmCalculadora (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Interprete Matematico", pos=wx.DefaultPosition, size=wx.Size(445, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(445, 276), wx.Size(445, 300))
        self.SetBackgroundColour(wx.Colour(197, 224, 241))

        self.m_menubar1 = wx.MenuBar(0)
        self.archivo = wx.Menu()
        self.salir = wx.MenuItem(self.archivo, ID_SALIR, u"Salir", wx.EmptyString, wx.ITEM_NORMAL)
        self.archivo.AppendItem(self.salir)

        self.m_menubar1.Append(self.archivo, u"Archivo")

        self.acercaDe = wx.Menu()
        self.calculadoraV01Wxpython = wx.MenuItem(self.acercaDe, ID_CALCULADORA_V01_WXPYTHON, u"Interprete Matematico v0.1 wxPython", wx.EmptyString, wx.ITEM_NORMAL)
        self.acercaDe.AppendItem(self.calculadoraV01Wxpython)

        self.m_menubar1.Append(self.acercaDe, u"Acerca de...")

        self.SetMenuBar(self.m_menubar1)

        fgSizer2 = wx.FlexGridSizer(1, 1, 2, 2)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer21 = wx.GridBagSizer(0, 0)
        gbSizer21.SetFlexibleDirection(wx.BOTH)
        gbSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer21.SetEmptyCellSize(wx.Size(40, 1))

        self.lblTexto = wx.StaticText(self, wx.ID_ANY, u"Interprete Matematico", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.lblTexto.Wrap(-1)
        self.lblTexto.SetFont(wx.Font(11, 74, 90, 92, True, "DejaVu Sans Mono"))

        gbSizer21.Add(self.lblTexto, wx.GBPosition(0, 0), wx.GBSpan(1, 11), wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        self.txtNumero = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(-1, -1), wx.TE_RICH | wx.TE_RICH2 | wx.TE_RIGHT)
        gbSizer21.Add(self.txtNumero, wx.GBPosition(1, 0), wx.GBSpan(1, 9), wx.ALIGN_CENTER | wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btnExpresion = wx.Button(self, ID_BTN_EXPRESION, u"Expresion", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer21.Add(self.btnExpresion, wx.GBPosition(1, 9), wx.GBSpan(1, 1), wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add(gbSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.TOP, 1)

        gbSizer2 = wx.GridBagSizer(1, 1)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gbSizer2.SetEmptyCellSize(wx.Size(10, 10))

        self.btnNumero1 = wx.Button(self, ID_BTN_1, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero2 = wx.Button(self, ID_BTN_2, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero2, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero3 = wx.Button(self, ID_BTN_3, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero3, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero4 = wx.Button(self, ID_BTN_4, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero4, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero5 = wx.Button(self, ID_BTN_5, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero5, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero6 = wx.Button(self, ID_BTN_6, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero6, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero7 = wx.Button(self, ID_BTN_7, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero7, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero8 = wx.Button(self, ID_BTN_8, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero8, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNumero9 = wx.Button(self, ID_BTN_9, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNumero9, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnNuemero0 = wx.Button(self, ID_BTN_0, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnNuemero0, wx.GBPosition(3, 0), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.btnBorrar = wx.Button(self, ID_BTN_BORRAR, u"Borrar", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnBorrar, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnSuma = wx.Button(self, ID_BTN_SUMA, u"+", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnSuma, wx.GBPosition(0, 3), wx.GBSpan(2, 1), wx.ALL | wx.EXPAND, 5)

        self.btnResta = wx.Button(self, ID_BTN_RESTA, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnResta, wx.GBPosition(2, 3), wx.GBSpan(2, 1), wx.ALL | wx.EXPAND, 5)

        self.btnMultiplicacion = wx.Button(self, ID_BTN_MULT, u"*", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnMultiplicacion, wx.GBPosition(0, 4), wx.GBSpan(2, 1), wx.ALL | wx.EXPAND, 5)

        self.btnDivicion = wx.Button(self, ID_BTN_DIVI, u"/", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btnDivicion, wx.GBPosition(2, 4), wx.GBSpan(2, 1), wx.ALL | wx.EXPAND, 5)

        self.btnCalcular = wx.Button(self, ID_BTN_CALC, u"Calcular", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnCalcular.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        gbSizer2.Add(self.btnCalcular, wx.GBPosition(4, 0), wx.GBSpan(1, 6), wx.ALL | wx.EXPAND, 5)

        fgSizer2.Add(gbSizer2, 1, wx.BOTTOM | wx.EXPAND, 5)

        self.SetSizer(fgSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.CerrarVentana, id=self.salir.GetId())
        self.Bind(wx.EVT_MENU, self.VentanaAcercaDe, id=self.calculadoraV01Wxpython.GetId())
        self.btnExpresion.Bind(wx.EVT_BUTTON, self.ingresarFuncion)
        self.btnNumero1.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero2.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero3.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero4.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero5.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero6.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero7.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero8.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNumero9.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnNuemero0.Bind(wx.EVT_BUTTON, self.nuevaCifra)
        self.btnBorrar.Bind(wx.EVT_BUTTON, self.eventoBorrar)
        self.btnSuma.Bind(wx.EVT_BUTTON, self.RealizarOperacion)
        self.btnResta.Bind(wx.EVT_BUTTON, self.RealizarOperacion)
        self.btnMultiplicacion.Bind(wx.EVT_BUTTON, self.RealizarOperacion)
        self.btnDivicion.Bind(wx.EVT_BUTTON, self.RealizarOperacion)
        self.btnCalcular.Bind(wx.EVT_BUTTON, self.CalcularResultado)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def CerrarVentana(self, event):
        event.Skip()

    def VentanaAcercaDe(self, event):
        event.Skip()

    def ingresarFuncion(self, event):
        evavaluador = EvaFuncion(self)
        evavaluador.Show()

    def nuevaCifra(self, event):
        event.Skip()

    def eventoBorrar(self, event):
        event.Skip()

    def RealizarOperacion(self, event):
        event.Skip()




    def CalcularResultado(self, event):
        event.Skip()


