import requests

class WrongPokemonName(Exception):
    pass

class WrongStation(Exception):
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


def user_input(dicOfStation):
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
            #let's break the loop, value has been iserted correctly
            break
    return answer

def get_data():
    pass

if __name__ == '__main__':
    pass
"""
webPage = "https://environment.data.gov.uk/hydrology/id/stations"

# fetching json request
jsonRequest = request_json(webPage)

# creation of dictionary of Station
dicOfStation = get_dictionary(jsonRequest)

# getting data from user and checking if value inserted exists in dictionary
user_input(dicOfStation)

#for key, value in dicOfStation.items():
#    print(key, value)
"""

req = requests.get("https://environment.data.gov.uk/hydrology/id/stations")
req = req.json()

for line in req['items']:
    for key, value in dict(line).items():
        
        print(key, value)






