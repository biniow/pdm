# -*- coding: utf-8 -*-

"""Plugin for json format support"""

import json


def read_json(input_file_path):
    """
    Function reads json file from path and returns list of records
    :param input_file_path: path to json input file
    :return: list of records
    """
    with open(input_file_path) as json_file:
        data = json.load(json_file)
        return list(data)
