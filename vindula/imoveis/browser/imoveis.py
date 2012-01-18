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
if 1==2:
    connection = Connection('localhost', 27017)
    db = connection['CoemiDB']
    db.add_son_manipulator(Transform())
    
    #Instancia a Collection
    imoveis_folder = ImovelCollection(db)
    cidades = []
    
    
    for imovel in  imoveis_folder.collection.find():
        cidades.append(imovel.getCidade())
        ufs.append(imovel.getUf())
        
    for cidade in cidades:
        print '%s %s' % (cidade.Nome,
                         cidade.Id)
    
    print imoveis_folder.collection.find({'Cidade_Id':5}).count()
    
    
    #        """
    #        ws_url = 'http://ws.wimoveis.com.br/default.asmx?WSDL'
    #        usuario_ws = '11165'
    #        senha_ws = 'abcd102030'
    #        client = Client(ws_url)
    #        logar =  client.service.logar(usuario_ws,senha_ws)
    #        #listarAluguel = client.service.listarAluguel(True)
    #        #pegarImovel = client.service.pegarImovel('136519')
    #        #print pegarImovel
    #        
    #        lista_alugueis = client.service.listarAluguel(True)
    #        lista_vendas = client.service.listarVenda(True)
    #        
    #        
    #        for imovel in lista_alugueis:
    #            imovel_obj = imoveis_folder.get(imovel.Id,params_obj=imovel)
    #        
    #        for imovel in lista_vendas:
    #            imovel_obj = imoveis_folder.get(imovel.Id,params_obj=imovel)
    #        
    #        """
    
    
#ws_url = 'http://ws.wimoveis.com.br/default.asmx?WSDL'
#usuario_ws = '181'
#senha_ws = 'imoveiscoemi123'
#client = Client(ws_url,timeout=600)
#logar =  client.service.logar(usuario_ws,senha_ws)
#listarAluguel = client.service.listarAluguel(True)
#pegarImovel = client.service.pegarImovel('136519')

# Menoti este método esta para ser resolvido, atualmente não esta funcionando
#lista_vendas = client.service.listarVendaRede()

#Este é o método utilizado atualmente
#lista_vendas_2 = client.service.listarVenda()
