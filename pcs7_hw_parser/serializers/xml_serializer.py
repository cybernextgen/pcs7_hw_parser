from models import Serializer
import dicttoxml
from xml.dom.minidom import parseString


class XMLSerializer(Serializer):
    """
    Serialize result to XML-file
    """
    serializer_name = 'xml'

    @staticmethod
    def __convert_channels_dict(module):
        ch = module.get('channels')
        if ch:
            module['channels'] = list(ch.values())
        return module

    def __init__(self, parent_args_parser):
        super(XMLSerializer, self).__init__(parent_args_parser=parent_args_parser)
        parent_args_parser.add_argument('--xml-pretty', action='store_true')
        parent_args_parser.add_argument('--xml-attr-type', action='store_true')

    def to_serial(self, args, data):
        temp = {}

        for key in data.keys():
            temp[key] = [self.__convert_channels_dict(m.__dict__) for m in data[key]]

        if args.xml_pretty:
            result = parseString(dicttoxml.dicttoxml(temp, attr_type=args.xml_attr_type)).toprettyxml().encode()
        else:
            result = dicttoxml.dicttoxml(temp, attr_type=args.xml_attr_type)

        args.output_file.write(result)
        args.output_file.close()
