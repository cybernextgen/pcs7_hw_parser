import os
"""
App settings
"""
# choose any supported by python runtime encoding
DEFAULT_INPUT_FILE_ENCODING = 'cp1251'

# tuple of parsers classes, you can specify custom parser here
PARSERS_AVAILABLE = (
    'dp_module_parser.DPModuleParser',
    'rack_module_parser.RackModuleParser'
)

# tuple of serializer classes, you can specify custom serializer here
SERIALIZERS_AVAILABLE = (
    'json_serializer.JSONSerializer',
    'xml_serializer.XMLSerializer',
    'pdf_serializer.PDFSerializer'
)

# verbose names for order numbers. Parsers fills 'module_type' field of model with values from that dict. Keys might be regex
MODULE_TYPES = {
    '6ES7 153-1\s*': 'IM153-1',
    '6ES7 153-2\s*': 'IM153-2',
    '6ES7 331-7KF\s*': 'SM331 AI 8',
    '6ES7 321-7BH\s*': 'SM321 DI 16x24v',
    '6ES7 321-7TH\s*': 'SM321 DI 16xNAMUR',
    '6ES7 322-1BF\s*': 'SM322 DO 8x24v',
    '6ES7 321-7RD\s*': 'SM321 DI 4xNAMUR',
    '6ES7 331-7PF\s*': 'SM331 AI 8xRTD',
    '6ES7 332-5RD\s*': 'SM332 AO 4 Ex',
    '6ES7 331-7SF\s*': 'SM331 AI 8xTC / 4xPT100',
    '6ES7 416-2XK\s*': 'CPU416-2',
    '6GK7 443-1EX\s*': 'CP443-1',
    '6ES7 405-0KA\s*': 'PS405',
    '6ES7 405-0KR\s*': 'PS405',
    '6ES7 341-1CH\s*': 'CP341 PtP / MODBUS',
    '6ES7 336-4GE\s*': 'SM336 F-AI 6, HART',
    '6ES7 326-1BK\s*': 'SM326 F-DI 24x24v',
    '6ES7 326-2BF10\s*': 'SM326 F-DO 10x24v',
    '6ES7 326-2BF01\s*': 'SM326 F-DO 10x24v',
    '6ES7 405-0KR00\s*': 'PS405 10A',
    '6ES7 416-5HS06\s*': 'CPU416-5H',
    '6ES7 332-5HD01\s*': 'SM332 AO 4',
    '6ES7 322-1BH01\s*': 'SM322 DO 16x24v',
    '6ES7 322-8BH01\s*': 'SM322 DO 16x24v DIAG',
    '6ES7 322-8BH10\s*': 'SM322 DO 16x24v DIAG',
    '6ES7 331-7RD00\s*': 'SM331 AI 4 Ex',
    '6ES7 417-4HT14\s*': 'CPU 417H',
    '6ES7 321-1BL00\s*': 'SM321 DI 32x24v',
    '6ES7 322-1BL00\s*': 'SM321 DO 32x24v',
    'SI1180FD.GSE': 'SIEMENS SIMOCODE pro V',
    '6ES7 350-2AH00\s*': 'FM350-2',
    'PAYLINK:6ES7 153-2BA02\s*': 'IM153-2HF / LINK',
    '6ES7 322-5SD00\s*': 'SM322 DO 4x24v Ex',
    'DIRI0948.GSD': 'DIRIS A40',
    'TELE0956.GSD': 'TELEMECANIQUE - ATV71/61'
}

# settings for PDF serializer
# path to folder with .svg labels templates
LABELS_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# mapping between module_type and .svg label template
LABELS_TEMPLATE_MAP = {
    'SM331 AI 8': '8_CH.svg',
    'SM322 DO 8x24v': '8_CH.svg',
    'SM331 AI 8xTC / 4xPT100': '8_CH_EX.svg',
    'SM331 AI 4 Ex': '4_CH_EX.svg',
    'SM321 DI 4xNAMUR': '4_CH_EX.svg',
    'SM332 AO 4 Ex': '4_CH_EX.svg',
    'SM332 AO 4': '4_CH.svg',
    'SM322 DO 4x24v Ex': '4_CH_EX.svg',
    'SM321 DI 16x24v': '16_CH_1.svg',
    'SM322 DO 16x24v DIAG': '16_CH_2.svg',
    'SM322 DO 16x24v': '16_CH_1.svg',
    'SM321 DI 16xNAMUR': '16_CH_2.svg',
    'SM331 AI 8xRTD': '8_CH_RTD.svg',
    'SM336 F-AI 6, HART': '6_CH_F.svg',
    'SM326 F-DI 24x24v': '24_CH_F.svg',
    'SM326 F-DO 10x24v': '10_CH_F.svg',
    'SM321 DI 32x24v': '32_CH.svg',
    'SM321 DO 32x24v': '32_CH.svg',
}

LABELS_REMOVED_CHARS = (
    'AE', 'DE', 'AI', 'DI', 'DO', 'AO', '_'
)
