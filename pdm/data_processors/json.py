# -*- coding: utf-8 -*-

"""Plugin for json format support"""

import json


def read_json(file_path):
    """
    Function reads json file from path and returns list of records
    :param file_path: path to json input file
    :return: list of records
    """
    with open(file_path) as input_file:
        data = json.load(input_file)
        return list(data)
