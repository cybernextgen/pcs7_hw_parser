#!/usr/bin/env python
import argparse
import logging
import settings
import pydoc
import os
import threading


def import_plugins(plugin_package, plugin_modules):
    plugins = []
    for plugin_path in plugin_modules:
        plugin_class = pydoc.locate('{}.{}'.format(plugin_package, plugin_path))
        if not plugin_class:
            logging.warning('Plugin "{}" not found'.format(plugin_class))
        else:
            plugins.append(plugin_class)
    return plugins


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        return arg


def main():
    parent_args_parser = argparse.ArgumentParser()

    parser_classes = import_plugins('parsers', settings.PARSERS_AVAILABLE)
    serializers_classes = import_plugins('serializers', settings.SERIALIZERS_AVAILABLE)

    serializers_pool = {cl.serializer_name: cl(parent_args_parser) for cl in serializers_classes}

    parent_args_parser.add_argument('--format', '-f', dest='output_format',
                                    choices=serializers_pool.keys(),
                                    default=serializers_classes[0].serializer_name,
                                    help="Output format")

    parent_args_parser.add_argument('--if', '-i', dest='input_file',
                                    required=True,
                                    help='Input SIMATIC HW CFG file',
                                    metavar='INPUT_FILE',
                                    type=lambda x: is_valid_file(parent_args_parser, x))

    parent_args_parser.add_argument('--of', '-o',
                                    dest='output_file',
                                    required=True,
                                    type=argparse.FileType('wb', 0),
                                    help='Output file name',
                                    metavar="OUTPUT_FILE")
    parent_args_parser.add_argument('--encoding', '-e',
                                    dest='input_file_encoding',
                                    default='cp1251',
                                    help='Input SIMATIC HW CFG file encoding')

    args = parent_args_parser.parse_args()
    try:
        threads = []
        result = {}

        with open(args.input_file, mode='r', encoding=args.input_file_encoding) as f:
            content = f.read()

        for cl in parser_classes:
            parser_instance = cl(result)
            threads.append(threading.Thread(target=parser_instance.parse, args=(content,)))

        for thread in threads:
            thread.daemon = True
            thread.start()

        for thread in threads:
            while thread.isAlive():
                thread.join(5)

        serializer = serializers_pool.get(args.output_format)
        serializer.to_serial(args, result)

    except (LookupError, UnicodeError) as e:
        logging.error('Exception while parse file, {}'.format(e))


if __name__ == '__main__':
    main()
