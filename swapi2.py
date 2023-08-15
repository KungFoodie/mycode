#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        pprint(vader)
        print("%s was born in the year %s. His eyes are now %s and his hair color is %s." % (vader['name'], vader['birth_year'], vader['eye_color'], vader['hair_color']))
        print("He first appeared in the movie %s and could be found flying around in his %s." % (requests.get(vader['films'][0]).json()['title'], requests.get(vader['starships'][0]).json()['name']))
    else:
        print("That is not a valid URL.")

    

if __name__ == "__main__":
    main()

