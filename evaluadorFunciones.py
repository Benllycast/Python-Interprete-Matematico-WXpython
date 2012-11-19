# To change this template, choose Tools | Templates
# and open the template in the editor.

from frmExpresiones import frmExpresiones
from Parseador_1 import *
import wx

class EvaFuncion(frmExpresiones):

    def __init__(self, parent):
	frmExpresiones.__init__(self, parent)

    def __del__(self):
        pass

    def evaluarFuncion(self, event):
	try:
	    expresion = self.txtFunciones.GetLineText(self.txtFunciones.GetNumberOfLines()-1)
	    ultima = parsear(expresion)
	    variableX = float(self.txtValueX.GetValue())
	    evaluada = fEvaluar(ultima, variableX)
	    respuesta = "\n->  "+str(evaluada)
	    self.txtFunciones.SetInsertionPointEnd()
	    self.txtFunciones.WriteText(respuesta)
	except Exception, e:
	    print "Exception: ", e
	    self.mostrarMensaje("Error","Ingrese una funcion")


    def mostrarMensaje(self, titulo, mensaje):
	dlg = wx.MessageDialog(self, mensaje,
			       titulo,
			       wx.OK | wx.ICON_INFORMATION
			       #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
			       )
        dlg.ShowModal()
        dlg.Destroy()