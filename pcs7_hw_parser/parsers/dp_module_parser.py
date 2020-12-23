import re
from models import DPModule
from models import Parser


class DPModuleParser(Parser):
    """
    Create DPModule objects from input file
    """
    def __init__(self, result):

        super(DPModuleParser, self).__init__(
            return_type=DPModule,
            reg_exp=r"(DPSUBSYSTEM (?P<dp_subsystem>[0-9]+), DPADDRESS (?P<dp_address>[0-9]+), (SLOT (?P<slot_num>[0-9]+), )?(\"(?P<order_num>((?!\").)+)\").?, (\"(?P<position_name>((?!\").)+)\")\s*((AUTOCREATED|REDUNDANT)\s*)?BEGIN(?P<specific_data>.*?)END\s\n+)",
            result=result
        )

        self.specific_data_reg_exp = r"(^SYMBOL\s+(?P<ch_type>.) , (?P<ch_number>[0-9]+), (\"(?P<ch_position_name>((?!\").)+)\"), (\"(?P<ch_description>((?!\").)+)\")\n)"

    def filter(self, fields):
        sd = fields.get('specific_data')
        del(fields['specific_data'])
        channels_data = dict()
        if sd:
            matches = re.finditer(
                self.specific_data_reg_exp,
                sd, re.DOTALL + re.M)
            for r in [m.groupdict() for m in matches]:
                channels_data[int(r['ch_number'])] = r

        fields['channels'] = channels_data
        return fields
