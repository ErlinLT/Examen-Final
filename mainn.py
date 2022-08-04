
from dao import *
from ui import *
from covidapi import apiCitas
import json


apicitas = apiCitas()


#print(json.dumps(apiData, indent=4))
crear()

#ram = random.random()
apid = apicitas.getReports()
print(apid)
#print(json.dumps(apidata, indent=4))



idioma = apid["language_code"]
frase = apid["content"]
autor = apid["id"]
print(idioma,frase,autor, sep="\t")
añadir(idioma,frase,autor)
print("CITAS", idioma, frase, autor, sep="\t")

print("="*40)
table_row(mostar())