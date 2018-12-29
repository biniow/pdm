# -*- coding: utf-8 -*-

"""Module contains basic classes for personal data management"""

import collections

from data_processors_registry import get_reader, get_writer


_PersonalData = collections.namedtuple('_PersonalData', 'name address phone_number')


class PersonalDataManager:
    """
    PersonalDataManager class is a wrapper for _PersonalData class instances
    """

    def __init__(self, input_data, skip_on_errors=False):
        """
        Initializes PersonalDataManager object
        :param input_data: iterable, should contains
        """
        self.data_records = set()

        for record in input_data:
            if isinstance(record, (tuple, list)):
                self.data_records.add(_PersonalData(*record))
            elif isinstance(record, dict):
                self.data_records.add(_PersonalData(**record))
            elif not skip_on_errors:
                exc_message = '{type_name} is not supported data type. Only tuples and/or dicts'.format(
                    type_name=type(record))
                raise TypeError(exc_message)

    @classmethod
    def read_from_format(cls, data_format, *args, **kwargs):
        """
        Method searches for specific reader in DataProcessorRegistry and read data using it
        :param data_format: data format specifies reader family
        :return: PersonalDataManger class with data read using specific reader
        """
        method = kwargs.get('method', 'default')
        skip_on_errors = kwargs.get('skip_on_errors', False)
        reader = get_reader(data_format, method)
        input_data = reader(*args, **kwargs)
        return cls(input_data, skip_on_errors=skip_on_errors)

    @classmethod
    def from_csv(cls, *args, **kwargs):
        """
        Wrapper for read_from_format for csv data type
        :return: PersonalDataManager class with data read from external source
        """
        return cls.read_from_format('csv', *args, **kwargs)

    @classmethod
    def from_json(cls, *args, **kwargs):
        """
        Wrapper for read_from_format for json data type
        :return: PersonalDataManager class with data read from external source
        """
        return cls.read_from_format('json', *args, **kwargs)

    def write_to_format(self, data_format, *args, **kwargs):
        """
        Method writes data to external storage in specific format
        :param data_format: data format specifies writer family
        :return: result of writing process
        """
        method = kwargs.get('method', 'default')
        writer = get_writer(data_format, method)
        return writer(self.data_records, *args, **kwargs)

    def to_text(self, *args, **kwargs):
        """
        Wrapper for write_to_format to text
        :return: result of writing process
        """
        return self.write_to_format('text', *args, **kwargs)

    def to_html(self, *args, **kwargs):
        """
        Wrapper for write_to_format to html
        :return: result of writing process
        """
        return self.write_to_format('html', *args, **kwargs)
