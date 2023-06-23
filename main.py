import random

import requests
from datetime import datetime
class WrongStation(Exception):
    pass
class WrongRangeChosen(Exception):
    pass

class WrongRange(Exception):
    pass

def request_json(webPage):

    req = requests.get(webPage)
    req = req.json()

    return req

def get_dictionary(jsonRequest):

    dictionary = {}
    label: str
    stationGuid: str

    for line in jsonRequest['items']:
        for key, value in dict(line).items():
            if key == 'stationGuid':
                stationGuid = value
            elif key == 'label':
                label = value

        dictionary.update({f'{label}': stationGuid})

    return dictionary

def initial_user_input(dicOfStation):
    while True:
        try:
            answer = str(input("Please provide Station Name or ID of station: "))

            if answer in ("", " "):
                raise TypeError

            if answer not in dicOfStation.values():
                if answer not in dicOfStation.keys():
                    raise WrongStation

        except TypeError:
            print("Sorry, you haven't provided any information, please try once again...")
            continue

        except WrongStation:
            print("Sorry, you haven't provided the right Station Name or ID of station")
            continue

        else:
            #let's break the loop, value has been inserted correctly
            break
    return answer


def get_basic_data(answer, dicOfStation):

    dictionary2 = {}
    key_tmp: str
    value_tmp: str
    req: dict

    # if user has provided name of station, this piece of code maps it to GUID based on dictionary
    if answer not in dicOfStation.values():
        for key, value in dicOfStation.items():
            if answer == key:
                answer = value

    req = requests.get(f"https://environment.data.gov.uk/hydrology/id/stations/{answer}")
    req = req.json()


    for line in req['items']:
        for key, value in dict(line).items():

            if key == 'label':
                value_tmp = value
                dictionary2.update({f'{"label"}': value_tmp})

            elif key == 'easting':
                value_tmp = value
                dictionary2.update({f'{"easting"}': value_tmp})

            elif key == 'lat':
                value_tmp = value
                dictionary2.update({f'{"lat"}': value_tmp})

            elif key == 'long':
                value_tmp = value
                dictionary2.update({f'{"lat"}': value_tmp})

            elif key == 'wiskiID':
                value_tmp = value
                dictionary2.update({f'{"wiskiID"}': value_tmp})

            elif key == 'gridReference':
                value_tmp = value
                dictionary2.update({f'{"gridReference"}': value_tmp})

            elif key == 'searchText':
                value_tmp = value
                dictionary2.update({f'{"searchText"}': value_tmp})

            elif key == 'riverName':
                value_tmp = value
                dictionary2.update({f'{"riverName"}': value_tmp})

            elif key == 'northing':
                value_tmp = value
                dictionary2.update({f'{"northing"}': value_tmp})

            elif key == 'dateOpened':
                value_tmp = value
                dictionary2.update({f'{"dateOpened"}': value_tmp})

    print("\n Basic information about chosen station:\n")
    for key, value in dictionary2.items():
        print(f"{key}:     ", value)

    return answer


def get_date_range():
    date_range = []

    answer = '48513a18-e485-4317-ae92-93bf4f7f3e54'

    req = requests.get(
        f"https://environment.data.gov.uk/hydrology/id/measures/{answer}-flow-i-900-m3s-qualified/readings?earliest")
    req = req.json()

    for line in req['items']:
        for key, value in dict(line).items():
            if key == 'date':
                date_range.append(value)

    req = requests.get(
        f"https://environment.data.gov.uk/hydrology/id/measures/{answer}-flow-i-900-m3s-qualified/readings?latest")
    req = req.json()

    for line in req['items']:
        for key, value in dict(line).items():
            if key == 'date':
                date_range.append(value)

    return date_range

def get_detailed_information(date_range):

    while True:
        try:
            print(f"\nFor the selected station, the date range is as follows: {date_range}")
            usr_input = input(f"Please choose one of available dates i.e {min(date_range)}: ")

            if usr_input in ("", " "):
                raise TypeError

            if not datetime.strptime(usr_input, '%Y-%m-%d'):
                raise ValueError

            if usr_input < min(date_range) or usr_input > max(date_range):
                raise WrongRange

        except TypeError:
            print("Sorry, you haven't provided any information, please try once again...")
            continue

        except ValueError:
            print("Sorry, you haven't provided date in the right format")
            continue

        except WrongRange:
            print("Sorry, you haven't provided available date per chosen Station")
            continue

        else:
            #let's break the loop, value has been inserted correctly
            break

    return usr_input

def get_station_details(answer, date_chosen):
    req = requests.get(
        f"https://environment.data.gov.uk/hydrology/id/measures/{answer}-flow-i-900-m3s-qualified/readings?date={date_chosen}")
    req = req.json()

    for line in req['items']:
        for key, value in dict(line).items():
            if key == "dateTime":
                print("\n")
            if key not in ("measure", "date"):
                print(f"{key}: ", f"\t\t\t{value}")



#Main function, running program
if __name__ == '__main__':
    pass

webPage = "https://environment.data.gov.uk/hydrology/id/stations"

# fetching json request
jsonRequest = request_json(webPage)

# creation of dictionary of Station
dicOfStation = get_dictionary(jsonRequest)

# getting data from user and checking if value inserted exists in dictionary
answer = initial_user_input(dicOfStation)

# getting basic information about particular station
answer = get_basic_data(answer, dicOfStation)

# getting range of available dates for chosen station
date_range = get_date_range()

# asking user to enter a date
date_chosen = get_detailed_information(date_range)

# showing details information about particular station
get_station_details(answer, date_chosen)










