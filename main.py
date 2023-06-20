import requests

class WrongPokemonName(Exception):
    pass

def request_json(webPage):

    req = requests.get(webPage)
    req = req.json()

    return req

def get_dictionary(jsonRequest):

    #req = requests.get("https://environment.data.gov.uk/hydrology/id/stations")
    #req = req.json()

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
            answer = str(input("Please provide ID of station: "))
            if answer in ("", " "):
                raise TypeError
            #if answer != "ditto":
                #raise WrongPokemonName

        except TypeError:
            print("Sorry, you haven't provided the right ID of station")
            continue

        except WrongPokemonName:
            print("You have choosen wrong Pokemon name")

        else:
            #let's break the loop, value has been iserted correctly
            break
    return answer


if __name__ == '__main__':
    pass

webPage = "https://environment.data.gov.uk/hydrology/id/stations"

# fetching json request
jsonRequest = request_json(webPage)

# creation of dictionary of Station
dicOfStation = get_dictionary(jsonRequest)

#user input
#user_input(dicOfStation)

for key, value in dicOfStation.items():
    print(key, value)












