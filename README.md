# SIMATIC PCS7/STEP7 hardware configuration parser

## Features
This parser allows you to export hardware configuration of your PCS7/STEP7 AS station to pretty json, or xml or custom format using 
plug-in serializers.

![Example of output json file](/images/json_example.png)

Another useful feature allows you to generate printable signal modules labels. For each module type you can define
svg file that contains label template.

![Example of printable labels](/images/labels_example.jpg)

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
```
