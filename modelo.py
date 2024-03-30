import Orange
import pickle
import pandas as pd
import inspect

class ModeloOrange:
    #abro el modelo       
    def saludo(self):
        print('hi esta es la clase modelo')
        
    def informe(self, datos):
        #listav = [1.0, 0.191489, 0.66038, 0.283582, 1.0, 0.0, 0.5, 0.666667, 0.666667, 0.0, 0.5, 0.0, 0.666667, 0.5, 0.333333, 0.75]
        #dominios = Domain(dominios)
        #print('Dominios ' , dominios)
        try:
          file ='arbol.pkcls'
          df=pickle.load(open(file,'rb'))
          print('Modelo cargado')
          result = df(datos)
          print(result)
          print('proceso terminad')
          return result
        except:
            print('Error al cargar el mdelo')
            return 'error'
      
         
    