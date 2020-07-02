import requests
from pyquery import PyQuery as pq

class Ciudadano:
    def __init__(self):
        self.__URL_CONSULTAS = 'https://eldni.com/buscar-por-dni'

    def get_essalud_informacion(self, dni):
        """
        Obtiene informacionde un dni desde ELDNI
        :param dni:
        :return: datos de la persona por el dni
        """
        url_reniec = "https://eldni.com/buscar-por-dni?dni="+dni+"&_token=H8N9fKdY0nyUtR2lHBLVQUSFpyrDJs8SCrn0elCM"
        HTML = requests.get(url=url_reniec).content
        jquery = pq(HTML)
        variables = jquery('td.text-left')

        nombres = ""
        paterno = ""
        materno = ""

        for indice, palabra in enumerate(variables.items()): 
            if indice == 0:
                nombres = palabra.text()
            elif indice == 1:
                paterno = palabra.text()
            else:
                materno = palabra.text()

        return {
            "dni": dni,
            "paterno": paterno,
            "materno": materno,
            "nombres": nombres
        }

