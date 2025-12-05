
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, datetime
from utils.states import States
class Jugador(SQLModel, table=True):
    id_jugador: Optional[int] = Field(default=None, primary_key=True, index=True)
    nombre_completo: str
    dorsal: int = Field(unique=True, index=True)
    fecha_nacimiento: date
    nacionalidad: str
    altura : float
    peso : int
    posicion: str
    estado: str = Field(description="Estado", default= States.ACTIVO.value)
    pie_dominate: str
    valor_mercado: float
    estadisticas : List["Estadistica"] = Relationship(back_populates="jugador")
    equipo : List["Equipo"] = Relationship(back_populates="jugador")

class Estadistica(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    minutos: int
    goles: int
    faltas: int
    id_tarjeta_FK: int = Field(foreign_key="tarjetas.id_tarjeta")
    id_jugador_FK: int = Field(foreign_key="jugador.id_jugador")
    id_partido_FK: int = Field(foreign_key="partido.id_partido")
    jugadores: Optional["Jugador"] = Relationship(back_populates="jugadores")
    partidos: Optional["Partido"] = Relationship(back_populates="partidos")
    tarjetas: Optional["Tarjeta"] = Relationship(back_populates="tarjetas")

class Tarjetas(SQLModel, table=True):
    pass


class Partido(SQLModel, table=True):
    id_partido: Optional[int] = Field(default=None, primary_key=True, index=True)



class Equipo(SQLModel, table=True):
    pass


class EquipoJugador(SQLModel, table=True):
    pass


class Tarjetas(SQLModel, table=True):
    id_tarjeta: Optional[int] = Field(default=None, primary_key=True, index=True)

