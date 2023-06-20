import requests, re
"""
class WrongPokemonName(Exception):
    pass


def user_input_dictionary():
    req = requests.get(f"https://environment.data.gov.uk/hydrology/id/stations")
    req = req.json()

    return dict(req)


def user_input():
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

def request_json(pokemon):

    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    pokemon = req.json()

    return dict(pokemon)
"""

if __name__ == '__main__':
    pass

#dicOfStation = user_input_dictionary()

"""
req = requests.get("https://environment.data.gov.uk/hydrology/id/stations")
person = req.json()

for film in person['items']:
    req = requests.get(film)
    film = req.json()
    print("Film is: ", film['@id'])


#answer = user_input()
#print(answer)

#pokeamon = request_json(answer)
#print(pokeamon)
#print(type(pokeamon))

"""
import json

req = """
{
   "book": [

      {
         "id": "01",
         "language": "Java",
         "edition": "third",
         "author": "Herbert Schildt"
      },

      {
         "id": "07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }

   ]
}
"""
person = json.loads(req)

"""
for line in person['book']:
    d = dict(line)


for k, v in d.items():
    print(k, v)
"""

for line in person['book']:
    for key, value in dict(line).items():
        print(key, value)




"""
print(person['book'])

pattern_without_braces = r'(?<=\[).*?(?=\])'
parts = re.findall(pattern_without_braces, str(person))
print(parts)
"""