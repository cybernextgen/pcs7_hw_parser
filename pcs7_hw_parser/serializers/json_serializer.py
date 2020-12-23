from models import Serializer


class JSONSerializer(Serializer):
    """
    Serialize result to JSON-file
    """
    def __init__(self, parent_args_parser):
        super(JSONSerializer, self).__init__(parent_args_parser=parent_args_parser)

        json_args_parser = self.parent_args_parser.add_subparsers(title="json", dest="json_parser_args").add_parser(name="to_json")
        json_args_parser.add_argument('--pretty', action='store_true')

    def to_serial(self, args):
        print(args)
