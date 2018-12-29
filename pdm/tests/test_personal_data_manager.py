# -*- coding: utf-8 -*-

"""Unittests for personal_data_manager module"""

from unittest import TestCase

from pdm.personal_data_manager import PersonalDataManager, _PersonalData


class TestPersonalDataManager(TestCase):

    def test_init_objectCreationWithEmptyData_objectCreatedWithNoData(self):
        # Arrange
        input_data = []

        # Act
        pdm = PersonalDataManager(input_data)

        # Assert
        self.assertEqual(0, len(pdm.data_records))
        self.assertIsInstance(pdm.data_records, set)

    def test_init_objectCreationWithValidData_objectCreatedWithProvidedData(self):
        # Arrange
        data_entry = ('name', 'address', 'phone_number')
        data_entry2 = ('name2', 'address2', 'phone_number2')
        input_data = [data_entry, data_entry2]

        # Act
        pdm = PersonalDataManager(input_data)

        # Assert
        self.assertEqual(2, len(pdm.data_records))

    def test_init_objectCreationWithDuplicatedData_validNUmberOfRecordsExists(self):
        # Arrange
        data_entry = ('name', 'address', 'phone_number')
        input_data = [data_entry, data_entry]

        # Act
        pdm = PersonalDataManager(input_data)

        # Assert
        self.assertEqual(1, len(pdm.data_records))

    def test_init_objectCreationFromTuplesAndDicts_dataRecordsRepresentedAsPersonalDataObjects(self):
        # Arrange
        data_entry = ('name', 'address', 'phone_number')
        data_entry2 = {'name': 'name2', 'address': 'address2', 'phone_number': 'phone_number2'}
        input_data = [data_entry, data_entry2]

        # Act
        pdm = PersonalDataManager(input_data)

        # Assert
        for obj in pdm.data_records:
            self.assertIsInstance(obj, _PersonalData)

    def test_init_objectCreationInvalidInputData_typeErrorRaised(self):
        # Arrange
        input_data = ['invalid_input_data']

        # Act / Assert
        self.assertRaises(TypeError, PersonalDataManager, input_data)

    def test_init_objectCreationInvalidInputData_validNumberOfRecordsExists(self):
        # Arrange
        input_data = ['invalid_input_data', ('name', 'address', 'phone_number')]

        # Act
        pdm = PersonalDataManager(input_data, skip_on_errors=True)

        # Assert
        self.assertEqual(1, len(pdm.data_records))
