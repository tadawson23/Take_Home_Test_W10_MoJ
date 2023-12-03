"""Tests the API extraction code"""

import unittest
from unittest.mock import patch, MagicMock
import pytest
from test_2 import get_nearest_courts, format_extracted_data, read_csv


def test_extracted_data_formatting():
    """Tests that the extracted data is formatted correctly"""
    assert format_extracted_data([
        [
            'Robert Loggia', 'Crown Court', 'NP108XG',
            'Newport (South Wales) Crown Court',
            '99450 Caerdydd/ Cardiff 5', 1.8]]) == [
        {'name': 'Robert Loggia',
         'desired_court': 'Crown Court',
         'home_postcode': 'NP108XG',
         'nearest_desired_court': 'Newport (South Wales) Crown Court',
         'dx_number': '99450 Caerdydd/ Cardiff 5',
         'distance_to_court': 1.8}
    ]


def test_csv_function_raises_error():
    """Tests that the CSV function raises an error 
    if input is not a string"""

    with pytest.raises(ValueError):
        read_csv(123)


def test_get_courts_function_raises_error():
    """Tests that the get_nearest_courts function raises an error 
    if input is not a list"""

    with pytest.raises(ValueError):
        get_nearest_courts(123)


def test_formatting_function_raises_error():
    """Tests that the formatting function raises an error 
    if input is not a list"""

    with pytest.raises(ValueError):
        format_extracted_data(123)


class TestApiExtractor(unittest.TestCase):
    @patch('requests.get')
    def test_correct_data_from_api(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{'name': 'Newport (South Wales) Crown Court',
                                            'lat': 51.5883810960804,
                                            'lon': -3.0049370680169,
                                            'number': 441, 'cci_code': None,
                                            'magistrate_code': None,
                                            'slug': 'newport-south-wales-crown-court',
                                            'types': ['Crown Court'],
                                            'areas_of_law': [
                                                {'name': 'Crime',
                                                 'external_link': None,
                                                 'display_url': None,
                                                 'external_link_desc': None,
                                                 'display_name': None,
                                                 'display_external_link': None}],
                                            'areas_of_law_spoe': [],
                                            'displayed': True, 'hide_aols': False,
                                            'dx_number': '99450 Caerdydd/ Cardiff 5',
                                            'distance': 1.8
                                            }]

        mock_requests_get.return_value = mock_response
        result = get_nearest_courts(
            [['Robert Loggia', 'NP108XG', 'Crown Court']]
        )

        self.assertEqual(result, [['Robert Loggia', 'Crown Court', 'NP108XG',
                                   'Newport (South Wales) Crown Court',
                                   '99450 Caerdydd/ Cardiff 5', 1.8]])
