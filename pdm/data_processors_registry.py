# -*- coding: utf-8 -*-

"""Module represents data processors registry responsible for storing and providing readers/writers
information of supported formats"""

import data_processors.csv
import data_processors.html
import data_processors.json
import data_processors.text

INPUT_FORMATS = {
    'csv': {
        'default': data_processors.csv.read_csv
    },
    'json': {
        'default': data_processors.json.read_json
    }
}

OUTPUT_FORMATS = {
    'text': {
        'default': data_processors.text.write_text_output
    },
    'html': {
        'default': data_processors.html.write_html_table
    }
}


def get_data_processor(available_processors, data_format, method):
    """
    Function returns data processor callable object defined in data_processors structure
    :param available_processors: structure of supported formats wit available methods. Should be nested dict (dict of dicts)
    :param data_format: specifies data format requested by user
    :param method: specifies method of selected format
    :return: callable object which will process data
    """
    try:
        data_processor = available_processors[data_format][method]
        if data_processor is None:
            raise NotImplementedError('Requested  data processor is None')
        elif not callable(data_processor):
            raise TypeError('{processor} is not callable'.format(processor=str(type(data_processor))))
        return data_processor
    except KeyError:
        exception_msg_details = {'data_format': data_format, 'method': method, 'data_processors': available_processors}
        msg = '{data_format} and/or {method} not defined in {data_processors}'.format(**exception_msg_details)
        raise AttributeError(msg)
