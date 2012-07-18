# -*- coding: utf-8 -*-
import pymongo
from suds.client import Client
from imoveis_base import *
from pymongo import Connection

#from zope.interface import implements
#from Products.Five import BrowserView
#from five import grok
#from Acquisition import aq_inner
#from vindula.imoveis.browser.interfaces import IImoveisView
##from plone.dexterity.utils import createContent
#from plone.dexterity.utils import createContentInContainer
#
#class ImoveisView(grok.View):
#    def getImoveis(self):
#if 1==2:
#    connection = Connection('localhost', 27017)
#    db = connection['coemi']
#    db.add_son_manipulator(Transform())
    
    #Instancia a Collection
#    imoveis_folder = ImovelCollection(db)
#    cidades = []
    
    
#    for imovel in  imoveis_folder.collection.find():
#        cidades.append(imovel.getCidade())
#        ufs.append(imovel.getUf())
        
#    for cidade in cidades:
#        print '%s %s' % (cidade.Nome,
#                         cidade.Id)
    
#    print imoveis_folder.collection.find({'Cidade_Id':5}).count()

    

#ws_url = 'http://ws.wimoveis.com.br/default.asmx?WSDL'
#usuario_ws = '181'
#senha_ws = 'imoveiscoemi123'
#lient = Client(ws_url,timeout=6000)
#logar =  client.service.logar(usuario_ws,senha_ws)
#pegarImovel = client.service.pegarImovel('136519')
#listarAluguel = client.service.listarAluguel(True)
#print pegarImovel
       
#lista_alugueis = client.service.listarAluguel(True)
#lista_vendas = client.service.listarVenda(True)
    #        
    #        
    #        for imovel in lista_alugueis:
    #            imovel_obj = imoveis_folder.get(imovel.Id,params_obj=imovel)
    #        
    #        for imovel in lista_vendas:
    #            imovel_obj = imoveis_folder.get(imovel.Id,params_obj=imovel)
    #        
    #        """
