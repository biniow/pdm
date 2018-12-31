# -*- coding: utf-8 -*-

"""Plugin for text format support"""


def write_text_output(data, output_file_path, verbose=False):
    """
    Function writes data to text file
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    :param verbose: defines if verbose mode
    """
    result = []
    for data_record in data:
        result.append(str(data_record))

    with open(output_file_path, 'w') as result_file:
        txt_output = '\n====================\n'.join(result)
        result_file.write(txt_output)

        if verbose:
            print(txt_output)
