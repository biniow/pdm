"""Module contains basic classes for personal data management"""
import collections

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
