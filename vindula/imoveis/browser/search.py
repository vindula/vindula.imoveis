from five import grok
from vindula.imoveis.models.collections import *
from Products.CMFPlone.interfaces import IPloneSiteRoot
from vindula.mongodbconnector.interfaces import IMongoDBConnector 
        
class SearchView(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('search-imoveis')
    
    def get_values_search(self):
        #import pdb;pdb.set_trace()
        pass

#       vars = {'situacao':ImovelCollection().getImovelbySituacao(),
#                'cidade':ImovelCollection().getImovelbyCidadeId(),
#                'bairro':ImovelCollection().getImovelbyBairro(),
#                'tipo':ImovelCollection().getImovelbyTipoImovel(),
#                }
#        return vars