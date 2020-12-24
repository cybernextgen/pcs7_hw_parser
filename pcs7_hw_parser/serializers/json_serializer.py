from models import Serializer
import json


class JSONSerializer(Serializer):
    """
    Serialize result to JSON-file
    """
    serializer_name = 'json'

    def __init__(self, parent_args_parser):
        super(JSONSerializer, self).__init__(parent_args_parser=parent_args_parser)
        parent_args_parser.add_argument('--json-pretty', '-p', action='store_true')

    def to_serial(self, args, data):
        temp = dict()

        for key in data.keys():
            temp[key] = [m.__dict__ for m in data[key]]

        if args.json_pretty:
            result = json.dumps(temp, ensure_ascii=False, indent=4, sort_keys=True)
        else:
            result = json.dumps(temp, ensure_ascii=False)

        args.output_file.write(result.encode())
