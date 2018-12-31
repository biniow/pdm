# -*- coding: utf-8 -*-

"""Module contains basic classes for personal data management"""

import collections

from pdm.data_processors_registry import INPUT_FORMATS, OUTPUT_FORMATS, get_data_processor


class _PersonalData(collections.namedtuple('_PersonalData', 'name address phone_number')):
    __slots__ = ()

    def __str__(self):
        """
        Generates string representation of _PersonalDataManager instance
        :return: str representation of object
        """
        return "Name: {name}\nAddress: {address}\nPhone number: {phone_number}".format(name=self.name,
                                                                                       address=self.address,
                                                                                       phone_number=self.phone_number)


class PersonalDataManager:
    """
    PersonalDataManager class is a wrapper set of _PersonalData class instances
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

    @staticmethod
    def get_supported_formats():
        """
        Return formats currently supported by data_processors_registry
        :return structure which describes supported formats
        """
        return {'INPUT_FORMATS': list(INPUT_FORMATS.keys()),
                'OUTPUT_FORMATS': list(OUTPUT_FORMATS.keys())}

    @classmethod
    def read_from(cls, data_format, *args, **kwargs):
        """
        Method searches for specific reader in DataProcessorRegistry and read data using it
        :param data_format: data format specifies reader family
        :return: PersonalDataManger class with data read using specific reader
        """
        method = kwargs.pop('method', 'default')
        skip_on_errors = kwargs.pop('skip_on_errors', False)
        reader = get_data_processor(INPUT_FORMATS, data_format, method)
        input_data = reader(*args, **kwargs)
        return cls(input_data, skip_on_errors=skip_on_errors)

    def write_to(self, data_format, *args, **kwargs):
        """
        Method writes data to external storage in specific format
        :param data_format: data format specifies writer family
        :return: result of writing process
        """
        method = kwargs.pop('method', 'default')
        writer = get_data_processor(OUTPUT_FORMATS, data_format, method)
        return writer(self.data_records, *args, **kwargs)
