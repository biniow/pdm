# -*- coding: utf-8 -*-

"""Plugin for csv format support"""

import csv


def read_csv(file_path, delimiter=','):
    """
    Function reads csv file and returns list of records
    :param file_path: path to csv file
    :param delimiter: fields separator in csv file
    :return: list of records
    """
    result = []
    with open(file_path, 'r') as csv_file:
        for row in csv.reader(csv_file, delimiter=delimiter):
            result.append(row)
    return result
