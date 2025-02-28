import json
import requests
import sys


class Actividad_1():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        sys.stdout.reconfigure(encoding='utf-8')

    def leer_api(self, url):
        # El get()método envía una solicitud de GET a la url especificada.
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self):
        pass

    #def escribir_txt(self,nombre_archivo="",datos=object):
    def escribir_json(self,nombre_archivo="",datos=None): # "" '' """ """
        if nombre_archivo=="":
            nombre_archivo="datos.json"
        if datos is None:
            datos = "No hay datos"
        ruta_json = "{}json/{}".format(self.ruta_static,nombre_archivo)
        try:
            with open(ruta_json, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
                #f.write(str(datos))
                #ajuste
        except Exception as e:
            print("Error:",e)

        return True # booleano True (1) False (0)

    #def graficar_rectas(self,recta_empinada, recta_plana, recta_abajo):
    #def graficar_rectas(self,a, n,x):
        # recta_empinada 0.0, recta_plana 0.0, recta_abajo 0.0 0.0=float 0=int 6545646546 = double
        #f = (a*x)**n
        #print("funcion_calculo:",f)--

# vamos crea una intancia de la clase
ingestion = Actividad_1()
#datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
#"https://api.nbp.pl/api/exchangerates/tables/{table}/"
#datos_json = ingestion.leer_api("https://api.nbp.pl/api/exchangerates/tables/B/")
datos_json = ingestion.leer_api("https://api-colombia.com/api/v1/Country/Colombia")
print("datos json:",datos_json)
if ingestion.escribir_json(nombre_archivo="entrega_actividad_1.json",datos=datos_json):
    print("se creo el archivo json")
#print("esta es la ruta statica :",ingestion.ruta_static)
#for n in  range(0,10):
    #ingestion.graficar_rectas(5, n, 5.4)




    