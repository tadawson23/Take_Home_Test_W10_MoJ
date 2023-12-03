"""Extracts information about relevant courts from API"""

import csv
import requests

API_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="
NAME_DICT_POSITION = 0
POSTCODE_DICT_POSITION = 1
DESIRED_COURT_POSITION = 2
SUCCESS_STATUS_CODE = 200


def read_csv(filename: str) -> list:
    """Reads the csv data on each person and returns it as a list"""

    if not isinstance(filename, str):
        raise ValueError("Input is not a sting.")

    people_data_list = []

    with open(filename, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            people_data_list.append(row)

    return people_data_list


def get_nearest_courts(people_list: list) -> list:
    """Accesses the API and returns the relevant 
    information to each individual
    """

    if not isinstance(people_list, list):
        raise ValueError("Input is not a list.")

    list_extracted_data = []

    for person in people_list:
        name = person[NAME_DICT_POSITION]
        postcode = person[POSTCODE_DICT_POSITION]
        desired_court = person[DESIRED_COURT_POSITION]
        api_url = f"{API_URL}{postcode}"
        response = requests.get(api_url, timeout=20)

        if response.status_code == SUCCESS_STATUS_CODE:
            data = response.json()

            for item in data:
                if 'types' in item and desired_court in item['types'] and 'distance' in item:
                    nearest_court_of_desired_type = item['name']
                    distance = item['distance']
                    dx_number = item.get('dx_number', 'N/A')

                    list_extracted_data.append(
                        [name, desired_court,
                         postcode,
                         nearest_court_of_desired_type,
                         dx_number, distance])
                    break

        else:
            raise ValueError("Data could not be extracted.")

    return list_extracted_data


def format_extracted_data(list_extracted_data: list) -> list[dict]:
    """Formats the extracted data in a dictionary"""

    if not isinstance(list_extracted_data, list):
        raise ValueError("Input is not a list.")

    list_of_dicts = []
    keys = ['name', 'desired_court', 'home_postcode',
            'nearest_desired_court', 'dx_number', 'distance_to_court']

    for item in list_extracted_data:
        data_dict = dict(zip(keys, item))
        list_of_dicts.append(data_dict)

    return list_of_dicts


if __name__ == "__main__":

    list_of_people = read_csv('people.csv')
    data_list = get_nearest_courts(list_of_people)
    print(format_extracted_data(data_list))
