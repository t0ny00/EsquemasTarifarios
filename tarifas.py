'''
Created on 11/2/2015

@author: Tony
'''
import datetime
from _decimal import *

def calcularEstadia(hora_entrada, hora_salida):
    estadia = hora_salida - hora_entrada
    horas_completas = estadia.seconds // 3600
    fraccion_hora = int(int(estadia.seconds%3600)/60) 
    return horas_completas,fraccion_hora
    
    
def costoHorasCompletas(horas,tarifa):
    return horas*tarifa

def costoFraccionHoraEsquema1(fraccion,tarifa):
    if fraccion == 0: return 0
    return tarifa

def costoFraccionHoraEsquema2(fraccion,tarifa):
    if fraccion == 0: return 0
    else :
        if fraccion <= 30: return (tarifa/2)
        return tarifa 
    
def costoFraccionHoraEsquema3(fraccion,tarifa):
    if fraccion == 0: return 0
    return fraccion*(tarifa/60)


if __name__ == "__main__":
    getcontext().prec = 2 
    getcontext().rounding = ROUND_UP 
    tarifa = Decimal(5)
    h1,h2 = calcularEstadia(datetime.datetime(4,4,4,7,50), datetime.datetime(4,4,4,14,55))  
    print(h1,h2)
    print(costoHorasCompletas(h1, 5))
    print(costoFraccionHoraEsquema1(h2, tarifa))
    print(costoFraccionHoraEsquema2(h2, tarifa))  
    print(costoFraccionHoraEsquema3(h2, tarifa)) 
