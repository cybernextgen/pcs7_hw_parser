import os
import argparse
import logging
import settings
import pydoc


def import_plugins(plugin_package, plugin_modules):
    plugins = []
    for plugin_path in plugin_modules:
        plugin_class = pydoc.locate('{}.{}'.format(plugin_package, plugin_path))
        if not plugin_class:
            logging.warning('Plugin "{}" not found'.format(plugin_class))
        else:
            plugins.append(plugin_class)
    return plugins


def main():
    parent_args_parser = argparse.ArgumentParser(add_help=False)

    result = {}

    parsers_pool = [cl(result) for cl in import_plugins('parsers', settings.PARSERS_AVAILABLE)]
    serializers_pool = [cl(parent_args_parser) for cl in import_plugins('serializers', settings.SERIALIZERS_AVAILABLE)]

    # json_serializer.JSONSerializer(parent_parser)
    print(vars(parent_args_parser.parse_args()))


if __name__ == '__main__':
    main()
