# -*- coding: utf-8 -*-

"""Plugin for html format support"""


def write_html_table(data, output_file_path, verbose=False, header=True):
    """
    Function reads input data and creates html file
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    :param verbose: defines if verbose mode
    :param header: defines if header should be also presented in output file
    """
    result = "<table border=\"1\">{head}{body}</table>"

    if data:
        columns_order = list(data)[0]._fields

        head = _generate_table_head(columns_order) if header else ""
        body = _generate_table_body(data, columns_order)

        with open(output_file_path, 'w') as result_file:
            html_result = result.format(head=head, body=body)
            result_file.write(html_result)

            if verbose:
                print(html_result)


def _generate_table_head(columns_order):
    """
    Function generates table header
    :param columns_order: iterable which contains order of columns to present
    :return: str with HTML code related to table header
    """
    result = "<thead>"
    for column_name in columns_order:
        result += "<th>{column_name}</th>".format(column_name=column_name)
    result += "</thead>"
    return result


def _generate_table_body(data, columns_order):
    """
    Function generates table body
    :param data: set of _PersonalData class objects
    :param columns_order: iterable which contains order of columns to present
    :return: str with HTML code related to table body
    """
    result = "<tbody>"
    for data_record in data:
        result += "<tr>"
        for column_name in columns_order:
            result += "<td>{value}</td>".format(value=getattr(data_record, column_name))
        result += "</tr>"
    result += "</tbody>"
    return result
