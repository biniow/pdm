# -*- coding: utf-8 -*-

"""Module represents data processors registry responsible for storing and providing readers/writers
information of supported formats"""

READERS = {
    'csv': {
        'default': None
    },
    'json': {
        'default': None
    }
}

WRITERS = {
    'text': {
        'default': None
    },
    'html': {
        'default': None
    }
}


def get_data_processor(data_processors, data_format, method):
    """
    Function returns data processor callable object defined in data_processors structure
    :param data_processors: structure of supported formats wit available methods. Should be nested dict (dict of dicts)
    :param data_format: specifies data format requested by user
    :param method: specifies method of selected format
    :return: callable object which will process data
    """
    try:
        data_processor = data_processors[data_format][method]
        if data_processor is None:
            raise NotImplementedError('Requested  data processor is None')
        elif not callable(data_processor):
            raise TypeError('{processor} is not callable'.format(processor=str(type(data_processor))))
        return data_processor
    except KeyError:
        exception_msg_details = {'data_format': data_format, 'method': method, 'data_processors': data_processors}
        msg = '{data_format} and/or {method} not defined in {data_processors}'.format(**exception_msg_details)
        raise AttributeError(msg)


def get_reader(data_format, method):
    """
    Wrapper for get_data_processor - search in readers structure automatically
    :param data_format: specifies data format requested by user
    :param method: specifies method of selected format
    :return: proper reader function basing on selected criteria
    """
    return get_data_processor(READERS, data_format, method)


def get_writer(data_format, method):
    """
    Wrapper for get_data_processor - search in writers structure automatically
    :param data_format: specifies data format requested by user
    :param method: specifies method of selected format
    :return: proper writer function basing on selected criteria
    """
    return get_data_processor(WRITERS, data_format, method)
