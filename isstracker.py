#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg


URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    timestamp = resp['timestamp']
    date = datetime.datetime.fromtimestamp(timestamp)
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']
    loc = rg.search((lat, lon))    

    print("CURRENT LOCATION OF THE ISS:\n")
    print(f"Timestamp: {date}")
    print(f"Lon: {lon}\nLat: {lat}")
    print(f"City/Country: {loc[0]['name']}, {loc[0]['cc']}")

if __name__ == "__main__":
    main()