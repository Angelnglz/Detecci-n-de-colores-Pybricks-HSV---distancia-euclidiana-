from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

sensor_color_izquierdo = ColorSensor(Port.A) #puerto sensor izquierdo
sensor_color_derecho = ColorSensor(Port.B) #puerto sensor derecho



# Valores HSV de referencia, es mejor usar unos valores unificados para el sensor izquierdo y derecho. En el mejor de los casos los dos sensores darán el mismo valor o parecidos, si no dan valores parecidos creo que es mejor hacer dos listas de refencia
blanco_hsv = (192, 5, 76)
negro_hsv = (240, 9, 13)
verde_hsv = (165, 69, 26)
plateado_hsv = (0, 0, 99)

# sensibilidades ajustables segun la necesidad, por defecto 1 no afecta en nada.
sensibilidad_blanco = 1
sensibilidad_negro = 1
sensibilidad_verde = 1
sensibilidad_plateado = 1

# Funcion que obtiene HSV segun el sensor a utilizar
def obtener_hsv(sensor):
    hsv = sensor.hsv()
    return hsv.h, hsv.s, hsv.v

# Función para detectar color segun el sensor a utilizar
def detectar_color(sensor):
    h, s, v = obtener_hsv(sensor)

    blanco_h, blanco_s, blanco_v = blanco_hsv
    negro_h, negro_s, negro_v = negro_hsv
    verde_h, verde_s, verde_v = verde_hsv
    plateado_h, plateado_s, plateado_v = plateado_hsv

    formula_blanco = ((h - blanco_h) ** 2 + (s - blanco_s) ** 2 + (v - blanco_v) ** 2) * sensibilidad_blanco
    formula_negro = ((h - negro_h) ** 2 + (s - negro_s) ** 2 + (v - negro_v) ** 2) * sensibilidad_negro
    formula_verde = ((h - verde_h) ** 2 + (s - verde_s) ** 2 + (v - verde_v) ** 2) * sensibilidad_verde
    formula_plateado = ((h - plateado_h) ** 2 + (s - plateado_s) ** 2 + (v - plateado_v) ** 2) * sensibilidad_plateado

    if formula_blanco < formula_negro and formula_blanco < formula_verde and formula_blanco < formula_plateado:
        return "blanco"
    elif formula_verde < formula_negro and formula_verde < formula_blanco and formula_verde < formula_plateado:
        return "verde"
    elif formula_negro < formula_blanco and formula_negro < formula_verde and formula_negro < formula_plateado:
        return "negro"
    elif formula_plateado < formula_blanco and formula_plateado < formula_negro and formula_plateado < formula_verde:
        return "plateado"
    else:
        return "no es ninguno"


#declarar las funciones sin ningun valor previamente ya que la vamos a utilizar como variables globales luego en de un ciclo, mas adelante en el programa para estructurar el rescue line
color_izquierdo = None
color_derecho = None

def update(): #funcion para actualiazr los sensores (agregar las otras variables para utilizar en el rescue line)
    global color_izquierdo, color_derecho #variables para los sensores
    
    color_izquierdo = detectar_color(sensor_color_izquierdo)
    color_derecho = detectar_color(sensor_color_derecho)



while True: #
    update()
    print("color izquierdo: ", color_izquierdo)
    print("color derecho: ", color_derecho)
    wait(500)

