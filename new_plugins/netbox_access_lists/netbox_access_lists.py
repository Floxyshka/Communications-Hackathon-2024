from extras.plugins import PluginConfig


class MyPluginConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = 'My Custom Plugin'
    version = '0.1'
    author = 'Daniel'
    author_email = 'your@email.com'
    description = 'A custom plugin for adding splice trays and couplers to NetBox.'
    base_url = 'netbox_access_lists'
    required_settings = []
    default_settings = {}
    min_version = '3.0.0'
    max_version = '3.99.9'
    caching_config = {}

    def ready(self):
        from .models import SpliceTray, Coupler
        self.add_to_menu('dcim', {
            'label': 'Splice Trays',
            'icon': 'mdi-soldering-iron',
            'url': 'plugins:netbox_access_lists:splicetray_list',
        })
        self.add_to_menu('dcim', {
            'label': 'Couplers',
            'icon': 'mdi-couple',
            'url': 'plugins:netbox_access_lists:coupler_list',
        })
