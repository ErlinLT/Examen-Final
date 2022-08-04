import requests
import json

class apiCitas():
    def getReports(self):
        url = "https://quotes15.p.rapidapi.com/quotes/random/"

        headers = {
            "X-RapidAPI-Key": "50d1bee5b5msh271662bea856a0fp1c4508jsn13927aa21ba6",
            "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        #print(response.text)
        return json.loads(response.text) #extrae una cadena de texto