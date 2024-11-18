from netbox.plugins import PluginConfig
from .navigation import menu_items

class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = ' NetBox Access Lists'
    description = 'Manage simple ACLs in NetBox'
    version = '0.1'
    base_url = 'access-lists'
    navigation = menu_items
    
config = NetBoxAccessListsConfig
