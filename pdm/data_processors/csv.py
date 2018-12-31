# -*- coding: utf-8 -*-

"""Plugin for csv format support"""

import csv


def read_csv(input_file_path, verbose=False, delimiter=','):
    """
    Function reads csv file and returns list of records
    :param input_file_path: path to csv file
    :param verbose: defines if verbose mode
    :param delimiter: fields separator in csv file
    :return: list of records
    """
    result = []
    with open(input_file_path) as csv_file:
        for row in csv.reader(csv_file, delimiter=delimiter):
            result.append(row)

    if verbose:
        print(result)

    return result


def write_csv(data, output_file_path, verbose=False, delimiter=','):
    """
    Function writes data in csv format
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    :param verbose: defines if verbose mode
    :param delimiter: fields separator in csv file
    """
    with open(output_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, dialect='excel', delimiter=delimiter)
        writer.writerows(data)

    if verbose:
        with open(output_file_path, 'r') as csv_file:
            print(csv_file.read())
