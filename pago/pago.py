from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Pago(BaseModel):
    producto: str
    monto: float

@app.post("/pago")
def pago(datos: Pago):

    response = requests.get(
        "http://procesapago-service:9090/procesa", # Llamada al servicio interno
        params={
            "producto": datos.producto,
            "monto": datos.monto
        }
    )

    return response.json()
