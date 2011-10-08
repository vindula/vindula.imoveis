# -*- coding: utf-8 -*-
from zope.interface import Interface

class IImoveisView(Interface):
    """ Interface for Imóveis"""
    def getImoveis():
        """ Return Imóveis """

