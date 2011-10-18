# -*- coding: utf-8 -*-
from datetime import datetime
from pymongo.son_manipulator import SONManipulator
from collections import *

class MongoPersistent(object):
    _type = ''
    attributes = ['_type',
                  'attributes',
                  ]
    primary_key = ''
    collection = ''
    
    def __init__(self,
                decode=None,
                write=False,
                **kwargs):
        """
        Initialize the object, and check if it must be decoded or saved at the mongodb's collection.
        """

        #Simple setting variables
        for key in kwargs.keys():
            setattr(self,key,kwargs.get(key))
        
        #Check if the object must be decoded
        #If decode != None is True, run the decode method.
        if decode != None:
            self.decode(decode)
        
        #If write is True, save the object at the mongodb's collection.
        if write == True:
            if self.collection.find({self.primary_key:getattr(self,self.primary_key)}).count() > 0:
                print self._type,' ja existe na base: ', getattr(self,self.primary_key)
            else:
                print 'Salvando %s: %s' % (self._type,getattr(self,self.primary_key))
                self.save()

        if write == True:
            self.CustomInit(kwargs)

    def CustomInit(self,kwargs):
        """
        This method should be overwritten
        """
        self.data_criacao_objeto = datetime.now()
        if 'params_obj' in kwargs.keys():
            self.salvaDadosWS(kwargs.get('params_obj'))
                
    def decode(self,vars):
        """Faz o decode do objeto, pegando o dicionario gravado no mongodb e colocando os valores nos devidos attributos."""                
        for key in vars.keys():
            setattr(self,key,vars[key])

    def encode(self):
        encoded = {}
        for field in self.attributes:
            encoded[field] = getattr(self,field)
        return encoded
        
    def save(self):
        self.collection.remove({self.primary_key:getattr(self,self.primary_key)})
        self.collection.insert({self.primary_key:self})

    def remove(self):
        self.collection.remove({self.primary_key:getattr(self,self.primary_key)})
        
    def salvaDadosWS(self,objeto_ws):
        """
        Recebe objeto do WS e salva os dados.
        """
        for param in dir(objeto_ws):
            if param in self.attributes:
                setattr(self,param,getattr(objeto_ws,param))
                
        self.CustomSalvaDados(objeto_ws)
        self.save()

    def CustomSalvaDados(self,objeto_ws):
        pass

class Imovel(MongoPersistent):          
    _type = 'Imovel'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'Id_antigo',
                  'Logradouro',
                  'Complemento',
                  'Cep',
                  'Descricao',
                  'DescricaoCompleta',
                  'ResumoEndereco',
                  'Quarto',
                  'Suite',
                  'AluguelGarantidows',
                  'descontoIRRFws',
                  'Banheiro',
                  'Lavabo',
                  'Elevador',
                  'Garagem',
                  'Dce',
                  'Armarios',
                  'Vazadows',
                  'Posicao',
                  'dataInclusao',
                  'dataAlteracao',
                  'Responsavel',
                  'Creci',
                  'Telefone1',
                  'Telefone2',
                  'Plantaws',
                  'Agiows',
                  'exibirPortalws',
                  'Exibirsitews',
                  'Exibirobraws',
                  'Destaquews',
                  'Ativows',
                  'areaTerrenostr',
                  'Areaverdestr',
                  'AreaCasaStr',
                  'areaConstruidoStr',
                  'Areatotalstr',
                  'Valorcondominiostr',
                  'Valorquitadostr',
                  'Valoragiostr',
                  'Valorstr',
                  'Valoradicionalstr',
                  'Valorquitadostr',
                  'Valoragiostr',
                  'Valorstr',
                  'Valoradicionalstr',
                  'Numeroapartemanto',
                  'Empreendimento',
                  'NumeroPasta',
                  'numeroContrato',
                  'dataOpcaoVenda',
                  'dataVencimento',
                  'Vista',
                  'Fachada',
                  'Andar',
                  'Andares',
                  'NumeroIPTU',
                  'numeroIPTUBox',
                  'NumeroChave',
                  'SituacaoChave',
                  'Caracteristica',
                  'PosicaoSol',
                  'ValorAluguelStr',
                  'Prioridade',
                  'videoUrl',
                  'videoPath',
                  'videoPath2',
                  'videoPath3',
                  'Referencia',
                  'data_criacao_objeto',
                  'DataOpcaoVenda',
                  'ValorAluguelStr',
                  'Cidade_Id',
                  'Uf_Id',
                  'Regiao_Id',
                  'Bairro_Id',
                  'Situacao_Id',
                  'TipoImovel_Id',
                  'Aluguel',
                  'Venda',
                  ]
    Id = ''
    Id_antigo = None
    Logradouro = None
    Complemento = None
    Cep = None
    Descricao = None
    DescricaoCompleta = None
    ResumoEndereco = None
    Quarto = None
    Suite = None
    AluguelGarantidows = None
    descontoIRRFws = None
    Banheiro = None
    Lavabo = None
    Elevador = None
    Garagem = None
    Dce = None
    Armarios = None
    Vazadows = None
    Posicao = None
    dataInclusao = None
    dataAlteracao = None
    Responsavel = None
    Creci = None
    Telefone1 = None
    Telefone2 = None
    Plantaws = None
    Agiows = None
    exibirPortalws = None
    Exibirsitews = None
    Exibirobraws = None
    Destaquews = None
    Ativows = None
    areaTerrenostr = None
    Areaverdestr = None
    AreaCasaStr  = None
    areaConstruidoStr = None
    Areatotalstr = None
    Valorcondominiostr = None
    Valorquitadostr = None
    Valoragiostr = None
    Valorstr = None
    Valoradicionalstr = None
    Valorquitadostr = None
    Valoragiostr = None
    Valorstr = None
    Valoradicionalstr = None
    Numeroapartemanto = None
    Empreendimento = None
    NumeroPasta = None
    numeroContrato = None
    dataOpcaoVenda = None
    dataVencimento = None
    Vista = None
    Fachada = None
    Andar = None
    Andares = None
    NumeroIPTU = None
    numeroIPTUBox = None
    NumeroChave = None
    SituacaoChave = None
    Caracteristica = None
    PosicaoSol  = None
    ValorAluguelStr  = None
    Prioridade = None
    videoUrl = None
    videoPath = None
    videoPath2 = None
    videoPath3 = None
    Referencia = None
    data_criacao_objeto = None
    DataOpcaoVenda = None
    DataVencimento = None
    ValorAluguelStr = None
    Cidade_Id = None
    Uf_Id = None
    Regiao_Id = None
    Bairro_Id = None
    Situacao_Id = None
    TipoImovel_Id = None
    Aluguel = False
    Venda = False
    
    def CustomSalvaDados(self,objeto_ws):
        from collections import *
        self.Cidade_Id = objeto_ws.Cidade.Id
        #Pesquisando se existe a cidade, senao existir cria.
        CidadeCollection(self.collection.database).get(objeto_ws.Cidade.Id,params_obj=objeto_ws.Cidade)
        
        self.Uf_Id = objeto_ws.Uf.Uf
        #Pesquisando se existe a UF, senao existir cria.
        UfCollection(self.collection.database).get(objeto_ws.Uf.Uf,params_obj=objeto_ws.Uf)
        
        self.Regiao_Id = objeto_ws.Regiao.Id
        #Pesquisando se existe a Regiao, senao existir cria.
        RegiaoCollection(self.collection.database).get(objeto_ws.Regiao.Id,params_obj=objeto_ws.Regiao)
        
        self.Bairro_Id = objeto_ws.Bairro.Id
        #Pesquisando se existe o Bairro, senao existir cria.
        BairroCollection(self.collection.database).get(objeto_ws.Bairro.Id,params_obj=objeto_ws.Bairro)
        
        self.Situacao_Id = objeto_ws.Situacao.Id
        #Pesquisando se existe a Situacao, senao existir cria.
        SituacaoCollection(self.collection.database).get(objeto_ws.Situacao.Id,params_obj=objeto_ws.Situacao)
        
        self.TipoImovel_Id = objeto_ws.Tipo.Id
        #Pesquisando se existe a Situacao, senao existir cria.
        TipoImovelCollection(self.collection.database).get(objeto_ws.Tipo.Id,params_obj=objeto_ws.Tipo)
        
        #self.FotoImovel_Id = objeto_ws.Foto.Id
        #Pesquisando se existe a Foto, senao existir cria.
        #FotoImovelCollection(self.collection.database).get(objeto_ws.Foto.Id,params_obj=objeto_ws.Foto)
        self.save()
        
    def getCidade(self):
        cidade = CidadeCollection(self.collection.database).get(self.Cidade_Id)
        return cidade
    
    def getUf(self):
        uf = UfCollection(self.collection.database).get(self.Uf_Id)
        return uf
    
    def getRegiao(self):
        from collections import RegiaoCollection
        regiao = RegiaoCollection(self.collection.database).get(self.Regiao_Id)
        return regiao
    
    def getBairro(self):
        bairro = BairroCollection(self.collection.database).get(self.Bairro_Id)
    
    def getSituacao(self):
        situacao = SituacaoCollection(self.collection.database).get(self.Situacao_Id)
    
    def getTipoImovel(self):
        tipo_imovel = TipoImovelCollection(self.collection.database).get(self.TipoImovel_Id)
    
    def getFotos(self):
        from collections import FotoImovelCollection
        fotos_folder = FotoImovelCollection(self.collection.database)
        return fotos_folder.collection.find({'ImovelId':self.Id})
        
class Cidade(MongoPersistent):          
    _type = 'Cidade'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'data_criacao_objeto',
                  'Nome',
                  'GMapZoom',
                  'Latitude',
                  'Longitude',
                  ]
    
    Id = ''
    data_criacao_objeto = None
    Nome = None
    GMapZoom = None
    Latitude = None
    Longitude = None

class Uf(MongoPersistent):
    _type = 'Uf'
    primary_key = 'Uf'
    attributes = ['_type',
                  'Uf',
                  'Nome',
                  'IdCapital',
                  'GMapZoom',
                  'Latitude',
                  'Longitude',
                  ]
    Uf = ''
    Nome = None
    IdCapital = None
    GMapZoom = None
    Latitude = None
    Longitude = None

class Bairro(MongoPersistent):
    _type = 'Bairro'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'IdRegiao'
                  'Nome',
                  'GMapZoom',
                  'Latitude',
                  'Longitude',
                  'IdRegiaoNome',
                  ]
    Id = ''
    Id = None
    IdRegiao = None
    Nome = None
    GMapZoom = None
    Latitude = None
    Longitude = None
    IdRegiaoNome = None

class Situacao(MongoPersistent):
    _type = 'Situacao'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'Ativo'
                  'AtivoPortal',
                  'AtivoSite',
                  'Existe',
                  'AtivoAtivoPortal',
                  ]
    Id = ''
    Id = None
    Ativo = None
    AtivoPortal = None
    AtivoSite = None
    Existe = None
    AtivoAtivoPortal = None

class Regiao(MongoPersistent):
    _type = 'Regiao'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'Regiao_Id',
                  'IdCidade',
                  'Cidade_Id',
                  'Nome',
                  'GMapZoom',
                  'Latitude',
                  'Longitude',
                  ]
    Id = None
    Regiao_Id = None
    IdCidade = None
    Cidade_Id = None
    Nome = None
    GMapZoom = None
    Latitude = None
    Longitude = None

class TipoImovel(MongoPersistent):
    _type = 'TipoImovel'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'Descricao',
                  ]
    Id = ''
    Descricao = None

class FotoImovel(MongoPersistent):
    _type = 'FotoImovel'
    primary_key = 'Id'
    attributes = ['_type',
                  'Id',
                  'FotoImovel_Id',
                  'Fisico',
                  'Path',
                  'NomeArquivo',
                  'DataInclusao',
                  'DataAlteracao',
                  'AtivoWs',
                  'AtualizadoWs',
                  'Descricao',
                  'ImovelId'
                  ]
    Id = ''
    FotoImovel_Id = None
    Fisico = None
    Path = None
    NomeArquivo = None
    DataInclusao = None
    DataAlteracao = None
    AtivoWs = None
    AtualizadoWs = None
    Descricao = None
    ImovelId = None
    
    def getUrl(self):
        url = 'http://www.wimoveis.com.br/img/foto/%s/%s'
        url = url % (self.Path,self.NomeArquivo)
        return url
    
class Transform(SONManipulator):
    types = ['Imovel',
             'Cidade',
             'Uf',
             'Regiao',
             'Bairro',
             'Situacao',
             'TipoImovel',
             'FotoImovel',
             ]

    def transform_incoming(self, son, collection):
        for key in son.keys():
            for class_type in self.types:
                if isinstance(son[key],eval(class_type)):
                    son = son[key].encode()
        return son

    def transform_outgoing(self, son, collection):
        if son.get('_type',None) in self.types:
            son = eval(son.get('_type'))(decode=son)
            son.collection = collection
        return son
