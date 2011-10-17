# -*- coding: utf-8 -*-
from datetime import datetime
from pymongo.son_manipulator import SONManipulator
from pymongo import ASCENDING, DESCENDING
from vindula.imoveis.models.documents import *
from interfaces import ICollection

class BaseCollection(object):
    """
    Return the collection
    """
    collection = ''
    collection_name = ''
    db = ''
    key = ''
    
    def __init__(self,db):
        self.collection_name = self.collection
        self.db = db
        command = 'self.db.%s' % self.collection
        self.collection  = eval(command)
        self.createDefaultIndexes()
        self.createCustomtIndexes()
    
    def get(self,param,NoneVar=None,params_obj=None):
        obj = NoneVar
        query = self.collection.find({self.key:param})
        print 'Pesquisando %s: %s' % (self.collection_name,param)
        if query.count() > 0:
            obj = query[0]
        else:
            command = """
            %s(%s=param,
               collection=self.collection,
               write=True)
            """ % (self.collection_name,self.key)
            if params_obj != None:
                command = command.replace(')',',params_obj=params_obj)')
            command = command.replace(' ','').replace('\n','')
            obj = eval(command)
        return obj
    
    def remove(self,param):
        pass

    def createDefaultIndexes(self):
        """
        Create the default indexes
        """
        if len(self.collection.index_information().keys()) < 2:
            #Adicionando index
            print 'Creating Index - Collection: %s Key: %s' % (self.collection_name,self.key) 
            self.collection.create_index([(self.key, ASCENDING)])
    
    def createCustomtIndexes(self):
        pass

class ImovelCollection(BaseCollection):
    """
    Manage the Im�vel Collection
    """
    collection = 'Imovel'
    key =  'Id'

    def createCustomtIndexes(self):
        pass

    def getImovelbyCidadeId(self,cidade_id):
        return self.collection.find({'Cidade_Id':cidade_id})
    
    def getImovelbyUfId(self,uf_id):
        return self.collection.find({'Uf_Id':uf_id})
    
    def getImovelbyBairro(self,cidade_id,bairro_id):
        return self.collection.find({'Cidade_Id':cidade_id,'Bairro_Id':bairro_id})
    
    def getImovelAluguel(self):
        return self.collection.find({'Aluguel':True})
    
    def getImovelVenda(self):
        return self.collection.find({'Venda':True})
    
    def getCountSituacao(self,situacao_id):
        return self.collection.find({'Situacao_Id':situacao_id}).count()
    
    def getImovelById(self,imovel_id):
        return self.collection.find({'Id':imovel_id})
    
    def getImovelbyTipoImovel(self,tipoimovel_id):
        return self.collection.find({'TipoImovel_Id': tipoimovel_id}) 
        
class CidadeCollection(BaseCollection):
    """
    Manage the Cidade Collection
    """
    collection = 'Cidade'
    key =  'Id'

    def getCidades(self):
        return self.collection.find({})
    
    def getCidadeByTipo(self,tipo):
        if tipo == 1:
            campo = 'Venda'
        else:
            campo = 'Aluguel'
        
        imovel_folder = ImovelCollection(self.collection.database)
        busca = imovel_folder.find({campo:True})
        cidades = []
        for imovel in busca:
            cidades.append(imovel.getCidade())
            
        return cidades
            
    
    
class UfCollection(BaseCollection):
    """
    Manage the Uf Collection
    """
    collection = 'Uf'
    key =  'Id'

class RegiaoCollection(BaseCollection):
    """
    Manage the Regiao Collection
    """
    collection = 'Regiao'
    key = 'Id'
    
    def getRegiao(self):
        regiao = RegiaoCollection(self.collection.database).get(self.Regiao_Id)
        return regiao

class BairroCollection(BaseCollection):
    """
    Manage the Bairro Collection
    """
    collection = 'Bairro'
    key = 'Id'
    
class SituacaoCollection(BaseCollection):
    """
    Manage the Situcao Collection
    """
    collection = 'Situacao'
    key = 'Id'
    
    def getSituacoes(self):
        return self.collection.find({})

class FotoImovel(BaseCollection):
    """
    Manage the Bairro Collection
    """
    collection = 'Foto'
    key = 'Id'
    

class TipoImovelCollection(BaseCollection):
    """
        Manage the TipoImovel Collection
    """
    collection = 'TipoImovel'
    key = 'Id'
        
        
