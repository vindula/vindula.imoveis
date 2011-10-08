from five import grok
from plone.directives import dexterity, form
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import IPloneSiteRoot
from suds.client import Client

from vindula.mongodbconnector.interfaces import IMongoDBConnector
from vindula.imoveis.content.imovel import IImovel
from vindula.imoveis.content.interfaces import IImoveisControlPanel
from vindula.imoveis.models.collections import *
        
class WSIntegrationView(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('imoveis-wsimport')
    
    def getSettings(self):
        record_prefix = 'vindula.imoveis.content.interfaces.IImoveisControlPanel'
        registry = getUtility(IRegistry)
        vars = {'ws_integration':registry.records.get(record_prefix + '.ws_integration').value,
                'ws_address':registry.records.get(record_prefix + '.ws_address').value,
                'ws_user':registry.records.get(record_prefix + '.ws_user').value,
                'ws_password':registry.records.get(record_prefix + '.ws_password').value,
                'db_name':registry.records.get(record_prefix + '.db_name').value,
                'imoveis_venda':registry.records.get(record_prefix + '.imoveis_venda').value,
                'imoveis_aluguel':registry.records.get(record_prefix + '.imoveis_aluguel').value,
                }
        return vars
    
    def render(self):
        vars = self.getSettings()
        mongodb_tool = getUtility(IMongoDBConnector)
        db = mongodb_tool.getDBConnection(db_name=vars['db_name'],
                                          transformation_class=Transform)
        imoveis_folder = ImovelCollection(db)
        
        client = Client(vars['ws_address'])
        client.service.logar(vars['ws_user'],
                             vars['ws_password'])
        lista_alugueis = client.service.listarAluguel(True)
        if vars['ws_integration'] == True:
            print 'Importing Data form Ws: ', vars['ws_address']
            for imovel in lista_alugueis:
                imovel_obj = imoveis_folder.get(imovel.Id,params_obj=imovel)
        
        print 'Imoveis na base: ', imoveis_folder.collection.find().count()
        return vars
