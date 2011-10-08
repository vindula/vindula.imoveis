# coding=utf-8
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage

from vindula.imoveis import _

class IImovel(form.Schema):
    """Imovel
    """
    
    title = schema.TextLine(
            title=_(u"Código do imóvel"),
        )
    
    