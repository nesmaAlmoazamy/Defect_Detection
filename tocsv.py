import json
import os
import glob
import pandas as pd
import argparse
import xml.etree.ElementTree as ET


def __list_to_csv(annotations, output_file):
    column_name = [
        'filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'
    ]
    xml_df = pd.DataFrame(annotations, columns=column_name)
    xml_df.to_csv(output_file, index=None)


def xml_to_csv(xml_dir, output_file):
    """Reads all XML files, generated by labelImg, from a directory and generates a single CSV file"""
    annotations = []
    for xml_file in glob.glob(xml_dir + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text), member[0].text,
                     int(member[4][0].text), int(member[4][1].text),
                     int(member[4][2].text), int(member[4][3].text))
            annotations.append(value)

    __list_to_csv(annotations, output_file)


def json_to_csv(input_json, output_file):
    """Reads a JSON file, generated by the VGG Image Annotator, and generates a single CSV file"""
    with open(input_json) as f:
        images = json.load(f)

    annotations = []

    for entry in images:
        filename = images[entry]['filename']
        for region in images[entry]['regions']:
            c = region['region_attributes']['class']
            xmin = region['shape_attributes']['x']
            ymin = region['shape_attributes']['y']
            xmax = xmin + region['shape_attributes']['width']
            ymax = ymin + region['shape_attributes']['height']
            width = 0
            height = 0

            value = (filename, width, height, c, xmin, ymin, xmax, ymax)
            annotations.append(value)

    __list_to_csv(annotations, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        'Reads all XML files, generated by labelImg, from a directory and generates a single CSV file',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('type',
                        metavar='type',
                        default='xml',
                        choices=['xml', 'json'],
                        help='LabelImg XML or VIA JSON')
    parser.add_argument(
        'input',
        metavar='input',
        type=str,
        help=
        'Directory containing the XML files generated by labelImg or path to a single VIA JSON'
    )
    parser.add_argument('output_csv',
                        metavar='output_csv',
                        type=str,
                        help='Path where the CSV output will be created')

    args = parser.parse_args()

    if args.type == 'xml':
        xml_to_csv(args.input, args.output_csv)
    elif args.type == 'json':
        json_to_csv(args.input, args.output_csv)
