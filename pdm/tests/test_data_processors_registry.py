# -*- coding: utf-8 -*-

"""Unit tests for data processors registry module"""
from unittest import TestCase

from data_processors_registry import get_data_processor


class TestDataProcessorsRegistry(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_format = 'csv'
        self.method = 'default'

    def test_getDataProcessors_notExistingDataFormat_raiseAttributeError(self):
        # Arrange
        no_formats = {}

        # Act / Assert
        self.assertRaises(AttributeError, get_data_processor, no_formats, self.data_format, self.method)

    def test_getDataProcessors_notExistingMethod_raiseAttributeError(self):
        # Arrange
        no_methods = {
            'csv': {}
        }

        # Act / Arrange
        self.assertRaises(AttributeError, get_data_processor, no_methods, self.data_format, self.method)

    def test_getDataProcessors_existingDataProcessorIsNone_raiseNotImplementedError(self):
        # Arrange
        processors = {
            'csv': {
                'default': None
            }
        }

        # Act / Assert
        self.assertRaises(NotImplementedError, get_data_processor, processors, self.data_format, self.method)

    def test_getDatProcessors_existingDataProcessorIsNotCallable_raiseTypeError(self):
        # Arrange
        processors = {
            'csv': {
                'default': 'not callable str object'
            }
        }

        # Act / Assert
        self.assertRaises(TypeError, get_data_processor, processors, self.data_format, self.method)

    def test_getDataProcessors_validDataProcessorFound_returnsProperProcessor(self):
        # Arrange
        assigned_function = print
        processors = {
            'csv': {
                'default': assigned_function
            }
        }

        # Act
        returned_data_processor = get_data_processor(processors, self.data_format, self.method)

        # Assert
        self.assertIs(assigned_function, returned_data_processor)
