from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Modelos(Base):
    __tablename__ = "modelos_main"

    id = Column(Integer, primary_key=True)
  
    pais = Column(String)
    lugar_residencia = Column(String)
    dispo_viajes = Column(String)
    nombre = Column(String)
    edad = Column(Integer)
    sexo = Column(String)
    ocupacion = Column(String)
    nivel_academico = Column(String)
    estatura = Column(Integer)
    peso = Column(Integer)
    busto = Column(Integer)
    cintura = Column(Integer)
    cadera = Column(Integer)
    calzado = Column(Integer)
    color_pelo = Column(String)
    color_ojos = Column(String)
    tono_piel = Column(String)
    email = Column(String)
    telefono = Column(Integer)
    instagram = Column(String)
    facebook = Column(String)
    tiktok = Column(String)
    foto_completa_id = Column(String)
    perfil_completo_id = Column(String)
    portada_completo_id = Column(String)
    rostro_id = Column(String)
    rostro_perfil_id = Column(String)
    sonriendo_id = Column(String)
    
    


Base.metadata.create_all(engine)