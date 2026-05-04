import pandas as pd 
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()


class KPICalculator:
    def __init__(self):
        self.path = os.getenv('PATH')

    def loadandclean(self):
        ingresos = pd.read_excel(path,parse_dates=[['F/RECEPCION','HORA']])
        ingresos['F/INGRESO'] = ingresos['F/INGRESO'].dt.date
        ingresos['FECHAINGRESO'] = ingresos['F/INGRESO'].astype(str) + ' ' +ingresos['HORA.1'].astype(str)
        ingresos['FECHAINGRESO']=pd.to_datetime(ingresos['FECHAINGRESO'],errors='coerce')

        return ingresos

    def calculatekpi(self,ingresos):
        
        ingresos['HORASINGRESO'] = ingresos['FECHAINGRESO']-ingresos['F/RECEPCION_HORA']
        print(ingresos.HORASINGRESO.describe())
        #ingresos.HORASINGRESO.plot()
        input('Press enter to exit:')
        
if __name__ == '__main__':
    app = KPICalculator()
    r = app.loadandclean()
    app.calculatekpi(r)
    