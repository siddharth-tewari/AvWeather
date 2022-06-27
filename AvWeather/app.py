import requests

def data():
    airportInput = str(input("Enter ICAO code: "))
    MetarbaseURL = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/"
    TAFbaseurl = "https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/"
    TAFurl = TAFbaseurl + airportInput.upper() + ".TXT"
    Metarurl = MetarbaseURL + airportInput.upper() + ".TXT"
    r = requests.get(Metarurl)
    p = requests.get(TAFurl)
    print("---------- METAR REPORT ----------")
    print(r.text)
    print("---------- TAF REPORT ------------")
    print(p.text)


