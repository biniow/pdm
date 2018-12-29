# -*- coding: utf-8 -*-

"""Plugin for text format support"""


def write_text_output(data, output_file_path):
    """
    Function writes data to text file
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    """
    result = []
    for data_record in data:
        result.append(str(data_record))

    with open(output_file_path, 'w') as result_file:
        result_file.write('\n====================\n'.join(result))
