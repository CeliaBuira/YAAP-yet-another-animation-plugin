
# noinspection PyDocstring,PyPep8Naming
def classFactory(iface):
    """Launch of the plugin"""
    from .yaap import YAAPPlugin
    return YAAPPlugin(iface)