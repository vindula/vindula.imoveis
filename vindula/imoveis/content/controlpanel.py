from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.z3cform import layout
from logging import getLogger

from interfaces import IImoveisControlPanel

class ImoveisControlPanel(RegistryEditForm):
    schema = IImoveisControlPanel
        

ImoveisControlPanelView = layout.wrap_form(ImoveisControlPanel, ControlPanelFormWrapper)
ImoveisControlPanelView.label = u"Vindula: Imoveis settings"



