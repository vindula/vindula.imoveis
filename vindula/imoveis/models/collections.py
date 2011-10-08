# -*- coding: utf-8 -*-
from datetime import datetime
from pymongo.son_manipulator import SONManipulator
from pymongo import ASCENDING, DESCENDING
from vindula.imoveis.models.documents import *

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

class CidadeCollection(BaseCollection):
    """
    Manage the Cidade Collection
    """
    collection = 'Cidade'
    key =  'Id'

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