from models import RackModule
from models import Parser


class RackModuleParser(Parser):
    """
    Create RackModule objects from input file
    """
    def __init__(self, result, with_submodules=False):
        super(RackModuleParser, self).__init__(
            return_type=RackModule,
            reg_exp='(RACK (?P<rack_num>[0-9]+), ((SLOT (?P<slot_num>[0-9]+)), (SUBSLOT (?P<subslot_num>[0-9]+), )?)?("(?P<order_num>((?!").)+)").?("(?P<firmware_version>((?!").)+)")?, ("(?P<position_name>((?!").)+)")\s*(((?!RACK|END).)+)\s*END)',
            result=result
        )
        self.with_submodules = with_submodules

    def filter(self, fields):
        if not self.with_submodules:
            if fields.get('subslot_num') or not fields.get('slot_num'):
                return
        return fields
