"""
Entry point to the program. Contains argument parser and steers execution
"""

import argparse
import json

from personal_data_manager import PersonalDataManager


def parse_args():
    """
    Function parses input argument from CLI
    :return: parsed arguments as map of values
    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-l', '--list-supported-formats', action='store_true',
                        help='Prints currently supported formats')
    parser.add_argument('-s', '--spec-file', help='Path to file with input/output details specification')

    return parser.parse_args()


def parse_spec_file(file_path):
    """
    Function parses specfile and returns its content
    :param file_path: path to specfile
    :return: content of specfile
    """
    with open(file_path) as spec_file:
        return json.load(spec_file)


def perform_data_operation(input_format, input_args, output_format, output_args):
    """
    Performs data operation using PersonalDataManager
    :param input_format: input data format
    :param input_args: input data additional args
    :param output_format: output data formats
    :param output_args: output data additional args
    """
    pdm = PersonalDataManager.read_from(input_format, **input_args)
    pdm.write_to(output_format, **output_args)


def get_args_from_user(data_type):
    """
    Function gets information about data source/destination from CLI
    :param data_type: defines inserted data type input/output
    :return: dict with gathered data
    """
    print('========> {data_type} data details'.format(data_type=data_type.title()))
    data_format = input('Select data format: ')
    method = input('Select method for {data_format} [default]: '.format(data_format=data_format))
    if not method:
        method = 'default'
    file_path = input('Absolute path to {data_type} file: '.format(data_type=data_type))
    return {
        '{data_type}_format'.format(data_type=data_type): data_format,
        '{data_type}_args'.format(data_type=data_type): {'method': method, '{data_type}_file_path'.format(
            data_type=data_type): file_path}
    }


def run_interactive_mode():
    """
    Function handles interactive mode - process of gathering data from user
    """
    result = []
    number_of_executions = int(input('How many data operation would you like to perform?: '))
    for i in range(number_of_executions):
        result.append({**get_args_from_user('input'), **get_args_from_user('output')})

    print('For further executions you can use specfile with following content:')
    print(json.dumps(result))

    return result


if __name__ == '__main__':

    args = parse_args()

    if args.list_supported_formats:
        print(PersonalDataManager.get_supported_formats())
        exit(0)

    executions = parse_spec_file(args.spec_file) if args.spec_file else run_interactive_mode()
    for execution in executions:
        perform_data_operation(**execution)

    print('Done...')
    exit(0)
