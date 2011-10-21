# -*- coding: utf-8 -*-
from zope.interface import Interface

class IImoveisView(Interface):
    """ Interface for Imóveis"""
    def getImoveis():
        """ Return Imóveis """

class IIMovel(Interface):
    """ Interface for Content Type Imóvel """
    
    def getImovel():
        """ Take the field values of the Imóvel """