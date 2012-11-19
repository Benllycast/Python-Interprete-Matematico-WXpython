# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from ayudaEvaluador import ayudaEvaluador

ID_BTN_AYUDA = 1000

###########################################################################
## Class frmExpresiones
###########################################################################

class frmExpresiones (wx.Frame):

    def __init__(self, parent):
	wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Expreciones", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

	self.SetSizeHintsSz(wx.DefaultSize, wx.Size(500, 300))
	self.SetBackgroundColour(wx.Colour(192, 224, 241))

	bSizer2 = wx.BoxSizer(wx.VERTICAL)

	self.pnlTexto = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
	bSizer4 = wx.BoxSizer(wx.VERTICAL)

	self.txtFunciones = wx.TextCtrl(self.pnlTexto, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_PROCESS_ENTER | wx.VSCROLL)
	bSizer4.Add(self.txtFunciones, 1, wx.ALL | wx.EXPAND, 5)

	self.pnlTexto.SetSizer(bSizer4)
	self.pnlTexto.Layout()
	bSizer4.Fit(self.pnlTexto)
	bSizer2.Add(self.pnlTexto, 4, wx.EXPAND | wx.ALL, 5)

	self.pntHerramienta = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
	bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

	self.m_staticText4 = wx.StaticText(self.pntHerramienta, wx.ID_ANY, u"Ingrese un Valor para la Variable:", wx.DefaultPosition, wx.DefaultSize, 0)
	self.m_staticText4.Wrap(-1)
	bSizer3.Add(self.m_staticText4, 0, wx.ALIGN_CENTER | wx.ALL, 5)


	bSizer3.AddSpacer((0, 0), 1, wx.EXPAND, 5)

	self.txtValueX = wx.StaticText(self.pntHerramienta, wx.ID_ANY, u"X = ", wx.DefaultPosition, wx.DefaultSize, 0)
	self.txtValueX.Wrap(-1)
	bSizer3.Add(self.txtValueX, 0, wx.ALIGN_CENTER | wx.ALL, 5)

	self.txtValueX = wx.TextCtrl(self.pntHerramienta, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT)
	bSizer3.Add(self.txtValueX, 0, wx.ALIGN_CENTER_VERTICAL, 5)


	bSizer3.AddSpacer((0, 0), 1, wx.EXPAND, 5)

	self.btnAyuda = wx.Button(self.pntHerramienta, ID_BTN_AYUDA, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
	bSizer3.Add(self.btnAyuda, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

	self.pntHerramienta.SetSizer(bSizer3)
	self.pntHerramienta.Layout()
	bSizer3.Fit(self.pntHerramienta)
	bSizer2.Add(self.pntHerramienta, 1, wx.EXPAND | wx.ALL, 5)

	self.SetSizer(bSizer2)
	self.Layout()

	self.Centre(wx.BOTH)

	# Connect Events
	self.txtFunciones.Bind(wx.EVT_TEXT_ENTER, self.evaluarFuncion)
	self.btnAyuda.Bind(wx.EVT_BUTTON, self.mostrarAyuda)

    def __del__(self):
	pass


    # Virtual event handlers, overide them in your derived class
    def evaluarFuncion(self, event):
	event.Skip()

    def mostrarAyuda(self, event):
	ayuda = ayudaEvaluador(self)
	ayuda.Show(1)


