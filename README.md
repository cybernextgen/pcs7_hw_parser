# SIMATIC PCS7/STEP7 hardware configuration parser [![Build Status](https://travis-ci.com/cybernextgen/pcs7_hw_parser.svg?branch=master)](https://travis-ci.com/cybernextgen/pcs7_hw_parser) [![codecov](https://codecov.io/gh/cybernextgen/pcs7_hw_parser/branch/master/graph/badge.svg?token=2R5PB6Z6KG)](https://codecov.io/gh/cybernextgen/pcs7_hw_parser)

## Features
This parser allows you to export hardware configuration of your PCS7/STEP7 AS station to pretty json, or xml or custom format using 
plug-in serializers.

![Example of output json file](/images/json_example.png)

Another useful feature allows you to generate printable signal modules labels. For each module type you can define
svg file that contains label template.

![Example of printable labels](/images/labels_example.jpg)

## Installation

Required python version >= 3.6

```sh
$ git clone https://github.com/cybernextgen/pcs7_hw_parser.git
$ cd pcs7_hw_parser
$ pip install -r pcs7_hw_parser/requirements.txt
```

## Configuration

Use `settings.py` module for overriding or extending default configuration

```py
# choose any supported by python runtime encoding
DEFAULT_INPUT_FILE_ENCODING = 'cp1251'

# tuple of parsers classes, you can specify custom parser here
PARSERS_AVAILABLE = (...)

# tuple of serializer classes, you can specify custom serializer here
SERIALIZERS_AVAILABLE = (...)

# verbose names for order numbers. Parsers fills 'module_type' field of model with values from that dict. Keys might be regex
MODULE_TYPES = { 'regex': 'module_type_verbose name'}

# settings for PDF serializer
# path to folder with .svg labels templates
LABELS_TEMPLATE_DIR = ...

# mapping between module_type and .svg label template
LABELS_TEMPLATE_MAP = {'module_type_verbose name': file.svg}

# chars from that tuple will be removed during labels rendering, when you select --pdf-strip-names option
LABELS_REMOVED_CHARS = ()
```

## Usage

CFG files must be exported from HW Config tool in human-readable format as shown below. 

![AS station export dialog](/images/export_dialog.png)

Typical parser usage:
```sh
# using default cp1251 encoding for cfg file and json output serializer
./app.py --if as.cfg --of as.json
# or simple
./app.py -i as.cfg -o as.json

# using specified serializer with option "json pretty print"
./app.py --format json --json-pretty --if as.cfg --of as.json
# or simple
./app.py -f json -p -i as.cfg -o as.json

# using custom cfg file encoding
./app.py --encoding utf-8 --if as.cfg --of as.json
# or simple
./app.py -e cp1251 -i as.cfg -o as.json

# using xml serializer with "xml pretty print" and attribute type declaration
./app --format xml --xml-pretty --xml-attr-type --if as.cfg --of as.xml

# using pdf serializer for printable labels generation
./app --format pdf --if as.cfg --of as.pdf
# more settings
# sheet bounds offset
./app --format pdf --pdf-x-offset 5 --pdf-y-offset 5 --if as.cfg --of as.pdf
# Gaps between labels
./app --format pdf --pdf-rows-margin 2 --pdf-cols-margin 2 --if as.cfg --of as.pdf
# Zooming if neccesery
./app --format pdf --pdf-zoom 0.95 --if as.cfg --of as.pdf
./app --format pdf --pdf-zoom 1.05 --if as.cfg --of as.pdf
# removing useless chars using settings.LABELS_REMOVED_CHARS tuple
./app --format pdf --pdf-strip-names --if as.cfg --of as.pdf
# change page size and page orientation (default: A4 portrait)
./app --format pdf --pdf-page-orientation l --pdf-page-size a3 --if as.cfg --of as.pdf
```
