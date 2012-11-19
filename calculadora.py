#-*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from frmCalculadora import *
from dlgAcercaDe import dlgAcercaDe
import wx

###########################################################################
## Class frmCalculadora
###########################################################################

class Calculadora (frmCalculadora):

    def __init__(self, parent):
        frmCalculadora.__init__(self, parent)
        ################################
        #parametros de calculo
        self.previo = 0
        self.operacion = 0
        self.nuevo = 0
        self.resultado = 0

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def CerrarVentana(self, event):
        event.Skip()
        print "hola Mundo"

    def VentanaAcercaDe(self, event):
        acercaDe = dlgAcercaDe(self)
        acercaDe.Show(1)
        del acercaDe

    def nuevaCifra(self, event):
        value = u''
        if self.txtNumero.GetValue() == "0":
            self.txtNumero.SetValue(value)
            
        if event.GetId() == ID_BTN_0:
            value = self.txtNumero.GetValue() + "0"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_1:
            value = self.txtNumero.GetValue() + "1"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_2:
            value = self.txtNumero.GetValue() + "2"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_3:
            value = self.txtNumero.GetValue() + "3"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_4:
            value = self.txtNumero.GetValue() + "4"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_5:
            value = self.txtNumero.GetValue() + "5"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_6:
            value = self.txtNumero.GetValue() + "6"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_7:
            value = self.txtNumero.GetValue() + "7"
            self.txtNumero.SetValue(value)

        if event.GetId() == ID_BTN_8:
            value = self.txtNumero.GetValue() + "8"
            self.txtNumero.SetValue(value)
            
        if event.GetId() == ID_BTN_9:
            value = self.txtNumero.GetValue() + "9"
            self.txtNumero.SetValue(value)


    def eventoBorrar(self, event):
        if event.GetId() == ID_BTN_BORRAR:
            self.previo = 0
            self.operacion = 0
            self.nuevo = 0
            self.resultado = 0
            self.txtNumero.SetValue("0")

    def RealizarOperacion(self, event):
        try:
            if self.txtNumero.IsEmpty():
                dlg = wx.MessageDialog(self, 'Ingrese un numero en el cuadro de texto',
                                       'A Message Box',
                                       wx.OK | wx.ICON_INFORMATION
                                       #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                       )
                dlg.ShowModal()
                dlg.Destroy()
            else:
                self.previo = float(self.txtNumero.GetValue())
                if event.GetId() == ID_BTN_SUMA:
                    self.operacion = ID_BTN_SUMA
                    self.txtNumero.SetValue("0")
                elif event.GetId() == ID_BTN_MULT:
                    self.operacion = ID_BTN_MULT
                    self.txtNumero.SetValue("0")

                elif event.GetId() == ID_BTN_RESTA:
                    self.operacion = ID_BTN_RESTA
                    self.txtNumero.SetValue("0")

                elif event.GetId() == ID_BTN_DIVI:
                    self.operacion = ID_BTN_DIVI
                    self.txtNumero.SetValue("0")

                else:
                    self.operacion = 0
        except Exception, e:
            self.previo = 0
            self.operacion = 0
            self.nuevo = 0
            self.resultado = 0
            self.txtNumero.SetValue(u"")
            print "Exception: ", e




    def CalcularResultado(self, event):
        if self.operacion == 0 or self.txtNumero.IsEmpty():
            dlg = wx.MessageDialog(self, 'precione en una operacion',
                                   'A Message Box',
                                   wx.OK | wx.ICON_INFORMATION
                                   #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        else:
            try:
                if self.operacion == ID_BTN_SUMA:
                    self.nuevo = float(self.txtNumero.GetValue())
                    self.resultado = self.previo + self.nuevo
                    self.previo = self.resultado
                    resultado = str(self.resultado)
                    self.txtNumero.SetValue(resultado)
                if self.operacion == ID_BTN_MULT:
                    self.nuevo = float(self.txtNumero.GetValue())
                    self.resultado = self.previo * self.nuevo
                    self.previo = self.resultado
                    resultado = str(self.resultado)
                    self.txtNumero.SetValue(resultado)
                if self.operacion == ID_BTN_RESTA:
                    self.nuevo = float(self.txtNumero.GetValue())
                    self.resultado = self.previo - self.nuevo
                    self.previo = self.resultado
                    resultado = str(self.resultado)
                    self.txtNumero.SetValue(resultado)
                if self.operacion == ID_BTN_DIVI:
                    self.nuevo = float(self.txtNumero.GetValue())
                    self.resultado = self.previo / self.nuevo
                    self.previo = self.resultado
                    resultado = str(self.resultado)
                    self.txtNumero.SetValue(resultado)
            except:
                dlg = wx.MessageDialog(self, 'Error al realizar la operacion',
                                       'A Message Box',
                                       wx.OK | wx.ICON_INFORMATION
                                       #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                       )
                dlg.ShowModal()
                dlg.Destroy()
                



if __name__ == "__main__":
    app = wx.App(False)
    frame = Calculadora(None)
    frame.Show()
        
    app.MainLoop()
