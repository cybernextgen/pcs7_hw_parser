import settings
import re
import os
import cairosvg
import tempfile
import logging
from fpdf import FPDF
from models import Serializer
from lxml import etree
from collections import defaultdict
from string import Formatter


class TemplateNotFound(Exception):
    pass


class TemplateRenderingException(Exception):
    pass


class PDFSerializer(Serializer):
    """
    Serialize result to PDF-file with printable labels
    """
    serializer_name = 'pdf'

    def __init__(self, parent_args_parser):
        super(PDFSerializer, self).__init__(parent_args_parser=parent_args_parser)
        parent_args_parser.add_argument('--pdf-x-offset', type=int, default=10, help="Offset between sheet x-bounds")
        parent_args_parser.add_argument('--pdf-y-offset', type=int, default=10, help="Offset between sheet y-bounds")
        parent_args_parser.add_argument('--pdf-zoom', type=float, default=1.0)
        parent_args_parser.add_argument('--pdf-rows-margin', type=int, default=0)
        parent_args_parser.add_argument('--pdf-cols-margin', type=int, default=0)
        parent_args_parser.add_argument('--pdf-strip-names', action='store_true')
        parent_args_parser.add_argument('--pdf-page-size', dest='page_size', choices=['a3', 'a4', 'a5'], default='a4',
                                        help="Page size")
        parent_args_parser.add_argument('--pdf-page-orientation', dest='page_orientation', choices=['l', 'p'],
                                        default='p', help="Page orientation (landscape/portrait)")

    @staticmethod
    def __ireplace(string, pattern, repl):
        """
        Replace case insensitive
        Raises ValueError if string not found
        """
        occurrences = re.findall(pattern, string, re.IGNORECASE)
        for occurrence in occurrences:
            string = string.replace(occurrence, repl)
        return string

    @staticmethod
    def __strip_position_name(name):
        for c in settings.LABELS_REMOVED_CHARS:
            name = PDFSerializer.__ireplace(name, c, '')
        return name

    @staticmethod
    def __get_template_path_for_module(m):
        if m.module_type in ['IM153-1', 'IM153-2']:
            raise TemplateNotFound

        file_name = settings.LABELS_TEMPLATE_MAP.get(m.module_type)
        if not file_name:
            logging.warning('Template for module {} not defined, using default.svg'.format(m.order_num))
            file_name = 'default.svg'

        template_path = os.path.join(settings.LABELS_TEMPLATE_DIR, file_name)
        return template_path

    @staticmethod
    def __render_template_for_module(m, args):
        try:
            with open(PDFSerializer.__get_template_path_for_module(m)) as src:
                content = src.read()

            dd = defaultdict(lambda: '')
            dd['m_p'] = m.position_name

            for k, value in m.channels.items():
                dd['ch{}'.format(value['ch_number'])] = PDFSerializer.__strip_position_name(
                    value['ch_position_name']) if args.pdf_strip_names else value['ch_position_name']

            content = Formatter().vformat(content, (), dd)
            xml_data = etree.fromstring(content.encode())

            label_width = int(xml_data.attrib['width'].replace('mm', ''))
            label_height = int(xml_data.attrib['height'].replace('mm', ''))

            res = tempfile.NamedTemporaryFile()
            cairosvg.svg2png(bytestring=content, write_to=res.name, dpi=400)

            return label_width, label_height, res
        except TemplateNotFound:
            logging.info('Template for module {} not found or not defined'.format(m.order_num))
            raise

    def to_serial(self, args, data):

        page_sizes_in_mm = {
            'a3': [297, 420],
            'a4': [210, 297],
            'a5': [148, 210]
        }

        page_size_x, page_size_y = page_sizes_in_mm.get(args.page_size, [210, 297])
        if args.page_orientation == 'l':
            page_size_x, page_size_y = page_size_y, page_size_x

        pdf = FPDF(orientation=args.page_orientation, format=args.page_size)

        current_x = args.pdf_x_offset
        current_y = args.pdf_y_offset

        pdf.add_page()
        row_height = 0
        for module in data.get('DPModule', []):
            try:
                label_width, label_height, res = self.__render_template_for_module(module, args)

                label_width = round(label_width * args.pdf_zoom)
                label_height = round(label_height * args.pdf_zoom)

                if label_height > row_height:
                    row_height = label_height

                if current_x + label_width + args.pdf_cols_margin + args.pdf_x_offset > page_size_x:
                    if current_y + row_height + label_height + args.pdf_rows_margin + args.pdf_y_offset > page_size_y:
                        pdf.add_page()
                        current_x = args.pdf_x_offset
                        current_y = args.pdf_y_offset
                    else:
                        current_x = args.pdf_x_offset
                        current_y = current_y + row_height + args.pdf_rows_margin

                pdf.image(res.name, current_x, current_y, label_width, label_height, type="png")

                current_x = current_x + label_width + args.pdf_cols_margin

            except TemplateNotFound:
                pass

        pdf.output(args.output_file.name, "F")
