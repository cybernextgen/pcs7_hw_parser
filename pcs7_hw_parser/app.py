import os
import argparse
import logging
import settings
from pydoc import locate


def dynamic_import(class_path):
    return locate(class_path)


def main():
    parent_args_parser = argparse.ArgumentParser(add_help=False)

    parsers_pool = []
    serializers_pool = []

    result = {}

    for parser_path in settings.PARSERS_AVAILABLE:
        parser_class = dynamic_import('parsers.{}'.format(parser_path))
        if not parser_class:
            logging.warning('Parser "{}" not found'.format(parser_class))
        else:
            parsers_pool.append(parser_class(result))

    for serializer_path in settings.SERIALIZERS_AVAILABLE:
        serializer_class = dynamic_import('serializers.{}'.format(serializer_path))
        if not serializer_class:
            logging.warning('Serializer "{}" not found'.format(serializer_class))
        else:
            serializers_pool.append(serializer_class(parent_args_parser))

    # json_serializer.JSONSerializer(parent_parser)
    print(vars(parent_args_parser.parse_args()))


if __name__ == '__main__':
    main()
