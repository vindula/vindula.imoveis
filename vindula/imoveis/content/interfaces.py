from zope.interface import Interface
from zope import schema


class IImoveisControlPanel(Interface):
    """
    MongoDB Connector interface
    """
    ws_integration = schema.Bool(title=u"Activate WS Integration",
                                 default=False)
    
    ws_address = schema.TextLine(title=u"WS Address",
                           default=u'http://ws.address')
    
    ws_user = schema.TextLine(title=u"WS username",
                              default=u"username")
    
    ws_password = schema.TextLine(title=u"WS password",
                              default=u"xxxxxxxx")
    
    db_name = schema.TextLine(title=u"Database name",
                              default=u"xxxxxxxx")
    
    imoveis_venda = schema.Bool(title=u"Imoveis Venda",
                                 default=True)
    
    imoveis_aluguel = schema.Bool(title=u"Imoveis Aluguel",
                                 default=True)
    