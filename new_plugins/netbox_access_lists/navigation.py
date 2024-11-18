from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu_items = (
        PluginMenuItem(
        link='plugins:netbox_access_lists:splice_tray_list',  
        link_text='Разварка муфты',
 ),
        PluginMenuItem(
        link='plugins:netbox_access_lists:coupler',  
        link_text='Mуфта',
 ),
)
