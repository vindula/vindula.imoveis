# coding=utf-8
from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText 
from plone.namedfile.field import NamedImage

#from z3c.relationfield.schema import RelationList, RelationChoice

from vindula.imoveis import _

class IImovel(form.Schema):
    """Imovel
    """
    
    title = schema.TextLine(
            title=_(u"Street"),
            description=_(u"Street of immobile"),
            required=True
        )
    
    code = schema.Int(
            title=_(u"Code immobile"),
            description=_(u"Code of immobile"),
            required=True
        )
    
    businnes = schema.Choice(
            title=_(u"Businnes"),
            description= _(u"Type of businnes"),
            values=[u'Sale', u'Rent', u'Season'],
            required=True
            )
            
    description_immobile = RichText(
        title=_(u"Description Immobile"),
        description=_(u"Description of immobile"),
        required=False,
        )
    
    number = schema.Int(
        title=_(u"Number"),
        description=_(u"Number of immobile"),
        required=False,
        )
    
    complement_address = schema.Text(
        title=_(u"Complement Address"),
        description=_(u"Information about the immobile"),
        required=False,
        )
    
    city = schema.TextLine(
        title=_(u"City"),
        description=_(u"City of immobile"),
        required=False,
        )
    
    location = schema.TextLine(
        title=_(u"Location"),
        description=_(u"Location of immobile"),
        required=False,
        )
    
    district = schema.TextLine(
        title=_(u"District"),
        description=_(u"District of immobile"),
        required=True,                   
        )
    
    cep = schema.TextLine(
        title=_(u"Cep"),
        description=_(u"Cep of immobile"),
        required=False,                   
        )
    
    type = schema.Choice(
            title=_(u"Type"),
            description= _(u"Type of immobile"),
            values=[u'Apart Hotel/Flat',
                    u'Apartment',
                    u'Apartment Coverage',
                    u'Apartment Duplex',
                    u'Apartment Furnished',
                    u'Barrack',
                    u'Building',
                    u'Chale',
                    u'Commerce',
                    u'Commercial Room',
                    u'Conjugate',
                    u'Condominium Lot',
                    u'Farm',
                    u'Farmstead',
                    u'Floor',
                    u'House',
                    u'House Condominium',
                    u'House Duplex',
                    u'House Furnished',
                    u'Garage',
                    u'Hangar',
                    u'Hotel',
                    u'Immobile Commerce',
                    u'Industry',
                    u'Inn',
                    u'Island',
                    u'Kiosk',
                    u'Kitinete',
                    u'Kitinete Furnished',
                    u'Loft',
                    u'Lot/Ground',
                    u'Mezzanine',
                    u'Others',
                    u'Release',
                    u'Room',
                    u'Season',
                    u'Sitio',
                    u'Sobrado',
                    u'Stables',
                    u'Store',
                    u'Vacancy',
                    u'Zone',
                    u'Zone Industrial',
                    ],
            required=True
            )
    
    area_private = schema.Int(
        title=_(u"Area Private"),
        description=_(u"Amount area private of immobile"),
        required=False,                   
        )
    
    area_ground = schema.Int(
        title=_(u"Area Ground"),
        description=_(u"Amount area ground of immobile"),
        required=False,                   
        )
    
    value_sale =  schema.Float(
        title=_(u"Value Sale"),
        description=_(u"Value Sale of immobile"),
        required=False,                   
        )
     
    value_rent = schema.Float(
        title=_(u"Value Rent"),
        description=_(u"Value Rent of immobile"),
        required=False,                   
        )
    
    phone1 = schema.TextLine(
        title=_(u"Phone 1"),
        description=_(u"Telephone 1 number for contact"),
        required=False,                   
        )
    
    phone2 = schema.TextLine(
        title=_(u"Phone 2"),
        description=_(u"Telephone 2 number for contact"),
        required=False,                   
        )
    
    condominium = schema.Float(
        title=_(u"Condominium"),
        description=_(u"Value condominium of immobile"),
        required=False,                   
        )
    
    room = schema.Int(
        title=_(u"Room"),
        description=_(u"Amount of room"),
        required=False,                   
        )
    
    suite = schema.Int(
        title=_(u"Suite"),
        description=_(u"Amount of suite"),
        required=False,                   
        ) 
    
    toilets = schema.Int(
        title=_(u"Toilets"),
        description=_(u"Amount of toilets"),
        required=False,                   
        )
    
    lavabo = schema.Bool(
        title=_(u"Lavago"),
        description=_(u"Lavabo"),
        required=False,                   
        )
    
    dce = schema.Int(
        title=_(u"DCE"),
        description=_(u"Number DCE"),
        required=False,                   
        )
    
    garage = schema.Int(
        title=_(u"Garage"),
        description=_(u"Amount of parking spaces"),
        required=False,                   
        )
    
    elevator = schema.Bool(
        title=_(u"Elevator"),
        description=_(u"Amount of elevator"),
        required=False,                   
        )
    
    pool = schema.Bool(
        title=_(u"Pool"),
        description=_(u"Amount of pool"),
        required=False,                   
        )
    
    floors = schema.Int(
        title=_(u"Floors"),
        description=_(u"Amount of floors"),
        required=False,                   
        )
    
    floor = schema.Int(
        title=_(u"Floor"),
        description=_(u"Number of floor"),
        required=False,                   
        )
    
    position_sun = schema.TextLine(
        title=_(u"Position Sol"),
        description=_(u"Position of the property in relation to sunrise"),
        required=False,                   
        )
    
    immobile_highlight = schema.Bool(
        title=_(u"Immobile Highlight"),
        description=_(u"Add immobile in the highlight"),
        required=False,                   
        )
    
    creci = schema.Int(
        title=_(u"Creci"),
        description=_(u"Creci"),
        required=True,                   
        )
class ImovelView(grok.View):
    grok.context(IImovel)
    grok.require('zope2.View')
    grok.name('view')
    
    def getImovel(self):
        imovel = self.context
        return imovel.__dict__ 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    