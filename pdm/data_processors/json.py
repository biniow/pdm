# -*- coding: utf-8 -*-

"""Plugin for json format support"""

import json


def read_json(input_file_path, verbose=False):
    """
    Function reads json file from path and returns list of records
    :param input_file_path: path to json input file
    :param verbose: defines if verbose mode
    :return: list of records
    """
    with open(input_file_path) as json_file:
        data = json.load(json_file)
        if verbose:
            print(data)
        return list(data)


def write_json(data, output_file_path, verbose=False):
    """
    Function writes data to json file
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    :param verbose: defines if verbose mode
    """
    result = []
    for data_record in data:
        result.append(data_record._asdict())

    with open(output_file_path, 'w') as output_file:
        json_output = json.dump(result, output_file)

        if verbose:
            print(json_output)
