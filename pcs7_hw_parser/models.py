import re, os
from settings import MODULE_TYPES


class Module(object):
    """
    Generic module class
    """
    def __init__(self, *args, **kwargs):
        self.order_num = kwargs.get('order_num')
        self.module_type = None
        self.position_name = kwargs.get('position_name')
        self.slot_num = kwargs.get('slot_num')
        self.fill_module_type()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def fill_module_type(self):
        for key in MODULE_TYPES:
            if re.match(key, self.order_num, re.IGNORECASE):
                self.module_type = MODULE_TYPES[key]
                break


class RackModule(Module):
    """
    Module and submodule which was inserted in central PLC rack
    """
    def __init__(self, *args, **kwargs):
        super(RackModule, self).__init__(*args, **kwargs)
        self.rack_num = kwargs.get('rack_num')
        self.subslot_num = kwargs.get('subslot_num')
        self.firmware_version = kwargs.get('firmware_version')


class DPModule(Module):
    """
    Module from DP-station
    """
    def __init__(self, *args, **kwargs):
        super(DPModule, self).__init__(args, **kwargs)
        self.dp_address = kwargs.get('dp_address')
        self.dp_subsystem = kwargs.get('dp_subsystem')
        self.channels = kwargs.get('channels')


def get_class_name(cls):
    return cls.__name__


class Parser(object):
    """
    Generic parser class
    """
    def __init__(self, return_type, reg_exp, result):
        self.return_type = return_type
        self.type_name = get_class_name(self.return_type)
        self.reg_exp = reg_exp
        self.result = result

    def filter(self, fields):
        return fields

    def parse(self, str_to_parse):
        res = list()

        matches = re.finditer(
            self.reg_exp,
            str_to_parse, re.DOTALL+re.M)

        for r in [m.groupdict() for m in matches]:
            r = self.filter(r)
            if r:
                res.append(self.return_type(**r))

        self.result[self.type_name] = res


class Serializer(object):
    """
    Generic serializer class
    """
    def __init__(self, parent_args_parser):
        self.parent_args_parser = parent_args_parser

    def to_serial(self, args, data):
        raise NotImplementedError
