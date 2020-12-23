# SIMATIC PCS7/STEP7 hardware configuration parser

## Features
This parser allows you to export hardware configuration of your PCS7/STEP7 AS station to pretty json, or xml or custom format using 
plug-in formatters. 

![Example of output json file](/images/json_example.png)

Another useful feature allows you to generate printable signal modules labels. For each module type you can define
svg file that contains label template.

![Example of printable labels](/images/labels_example.jpg)

## Usage

CFG files must be exported from HW Config tool in human-readable format as shown below. 

![AS station export dialog](/images/export_dialog.png)

Typical usage parser:
```sh
# using default cp1251 encoding for cfg file and json output serializer
./parser_cli.py --if as.cfg --of as.json

# using custom cfg file encoding and custom serializer
./parser_cli.py --encoding utf-8 --serializer xml --if as.cfg --of as.json 
```
