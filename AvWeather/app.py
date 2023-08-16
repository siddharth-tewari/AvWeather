import requests

def data():
    airportInput = str(input("Enter ICAO code: "))
    MetarbaseURL = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/"
    TAFbaseurl = "https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/"
    TAFurl = TAFbaseurl + airportInput.upper() + ".TXT"
    Metarurl = MetarbaseURL + airportInput.upper() + ".TXT"
    r = requests.get(Metarurl)
    p = requests.get(TAFurl)
    ask = input("Want Decoded METAR?: ")
    print("---------- METAR REPORT ----------")
    print(r.text)
    print("---------- TAF REPORT ------------")
    print(p.text)


    DecodedMetarbaseURL = "https://tgftp.nws.noaa.gov/data/observations/metar/decoded/"
    Decoded_Metarurl = DecodedMetarbaseURL + airportInput.upper() + ".TXT"
    d = requests.get(Decoded_Metarurl)
    if ask == "N":
        pass

    if ask == "Not":
        pass

    if ask == "n":
        pass

    if ask == "No":
        pass

    if ask == "no":
        pass

    else:
        print("---------- DECODED METAR REPORT ----------")
        print(d.text)
