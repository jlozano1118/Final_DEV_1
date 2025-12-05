from enum import Enum

class States(Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    LESIONADO= "LESIONADO"
    AMONESTADO= "AMONESTADO"

class Color(Enum):
    AMARILLA = "AMARILLA"
    ROJO = "ROJO"