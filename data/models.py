
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, datetime
from utils.states import States, Color
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
    tarjetas: Optional["Tarjetas"] = Relationship(back_populates="tarjetas")

class Tarjetas(SQLModel, table=True):

    id_tarjetas: Optional[int] = Field(default=None, primary_key=True, index=True)
    color: Color



class Partido(SQLModel, table=True):
    id_partido: Optional[int] = Field(default=None, primary_key=True, index=True)
    local: int = Field(foreign_key="Equipo.id_equipo")
    visitante: int = Field(foreign_key="Equipo.id_equipo")
    goles_local: int 
    goles_visitante: int 
    fecha: date
    equipolocal: Optional["Equipo"] = Relationship(back_populates="equipolocal")
    equipovisitante: Optional["Equipo"] = Relationship(back_populates="equipovisitante")

class Equipo(SQLModel, table=True):
    id_equipo: Optional[int] = Field(default=None, primary_key=True, index=True)
    nombre: str
    anio_fundacion: int
    ubicacion: str
    estadio: str

class EquipoJugador(SQLModel, table=True):
    id_equipo_jugador: Optional[int] = Field(default=None, primary_key=True, index=True)
    id_jugador_FK: int = Field(foreign_key="jugador.id_jugador")
    id_equipo_FK: int = Field(foreign_key="equipo.id_equipo")
    annio_ingreso: int
    jugadores: Optional["Jugador"] = Relationship(back_populates="jugadores")
    equipos: Optional["Equipo"] = Relationship(back_populates="equipos")

class JugadorCreate(SQLModel):
    nombre_completo: str
    dorsal: int
    fecha_nacimiento: date
    nacionalidad: str
    altura : float
    peso : int
    posicion: str
    pie_dominate: str
    valor_mercado: float

class EstadisticaCreate(SQLModel):
    minutos: int
    goles: int
    faltas: int
    id_tarjeta_FK: int 
    id_jugador_FK: int 
    id_partido_FK: int 


class PartidoCreate(SQLModel):
    local: int = Field(foreign_key="Equipo.id_equipo")
    visitante: int = Field(foreign_key="Equipo.id_equipo")
    goles_local: int 
    goles_visitante: int 
    fecha: date


class EquipoCreate(SQLModel):
    nombre: str
    anio_fundacion: int
    ubicacion: str
    estadio: str

class EquipoJugadorCreate(SQLModel):
    id_jugador_FK: int 
    id_equipo_FK: int 
    annio_ingreso: int

class TarjetasCreate(SQLModel):
    color: Color