# To change this template, choose Tools | Templates
# and open the template in the editor.


# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class dlgAcercaDe
###########################################################################

class dlgAcercaDe (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__ (self, parent, id=wx.ID_ANY, title=u"Acerca de...", pos=wx.DefaultPosition, size=wx.Size(-1, -1), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.Size(300, 400))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1.SetMinSize(wx.Size(199, 200))
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Interprete de Expreciones Matematicas v1.0\n\nCurso Python 2011- Universidad de Cartagena\nBenjamin E. Castillo Castro\nIng. Sistemas \n9 sem.\n\n\nSolo Uso Academico.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"logoUdc.jpg", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_bitmap1, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
	