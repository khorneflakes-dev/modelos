from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models import session, Modelos
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from uuid import uuid4 as uuid
import os

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer('/token')

fake_users_db = {
    'johndoe': {
        'username': 'khorne',
        'full_name': 'John Doe',
        'hashed_password': 'secret',
        'disabled': False
    },
    'alice': {
        'username': 'alice',
        'full_name': 'Alice Wonderson',
        'hashed_password': 'secret',
        'disabled': True
    }
}

# Configuración CORS
origins = ["http://localhost","http://localhost:5000","http://localhost:3000"]

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

folder = 'imagenes'
folder_path = os.path.join(os.getcwd(), folder)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

@app.post("/files2/")
async def create_file(
    file: UploadFile = File(...),
    fileb: UploadFile = File(...),
    token: str = Form(...),
):
    print(file.filename, fileb.filename, token)
    return file.filename, fileb.filename, token

@app.post('/files')
async def create_model(
    
    pais: str = Form(...),
    lugar_residencia: str = Form(...),
    dispo_viajes: str = Form(...),
    nombre: str = Form(...),
    edad: int = Form(...),
    sexo: str = Form(...),
    ocupacion: str = Form(...),
    nivel_academico: str = Form(...),
    estatura: int = Form(...),
    peso: int = Form(...),
    busto: int = Form(...),
    cintura: str = Form(...),
    cadera: str = Form(...),
    calzado: str = Form(...),
    color_pelo: str = Form(...),
    color_ojos: str = Form(...),
    tono_piel: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(...),
    instagram: str = Form(...),
    facebook: str = Form(...),
    tiktok: str = Form(...),
    foto1: UploadFile = File(...),
    foto2: UploadFile = File(...),
    foto3: UploadFile = File(...),
    foto4: UploadFile = File(...),
    foto5: UploadFile = File(...),
    foto6: UploadFile = File(...)
    ):
    image1 = str(uuid())
    image2 = str(uuid())
    image3 = str(uuid())
    image4 = str(uuid())
    image5 = str(uuid())
    image6 = str(uuid())
    
    modelo_formulario = Modelos(
        pais = pais,
        lugar_residencia = lugar_residencia,
        dispo_viajes = dispo_viajes,
        nombre = nombre,
        edad = edad,
        sexo = sexo,
        ocupacion = ocupacion,
        nivel_academico = nivel_academico,
        estatura = estatura,
        peso = peso,
        busto = busto,
        cintura = cintura,
        cadera = cadera,
        calzado = calzado,
        color_pelo = color_pelo,
        color_ojos = color_ojos,
        tono_piel = tono_piel,
        email = email,
        telefono = telefono,
        instagram = instagram,
        facebook = facebook,
        tiktok = tiktok,
        foto_completa_id = image1,
        perfil_completo_id = image2,
        portada_completo_id = image3,
        rostro_id = image4,
        rostro_perfil_id = image5,
        sonriendo_id = image6
    )
    session.add(modelo_formulario)
    session.commit()
    session.close()
    
    fotos = [foto1, foto2, foto3, foto4, foto5, foto6]
    images = [image1, image2, image3, image4, image5, image6]
    
    for i in range(len(fotos)):
        with open(f"{folder_path}/{images[i]}.{(fotos[i].filename).split('.')[-1]}", "wb") as image_aux:
            image_aux.write(await fotos[i].read())
    
    return {'message': 'formulario cargado exitosamente'}


@app.get('/users/me')
def user(token: str = Depends(oauth2_scheme)):
    return 'Hi'

@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get()
    if not user:
        raise HTTPException(status_code=400, detail='invalid user or password')
    if not form_data.password == user['hashed_password']:
        raise HTTPException(status_code=400, detail='invalid user or password')
        
    return {
        'access_token': 'tomate',
        'token_type': 'bearer'
    }