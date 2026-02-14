from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import requests

app = FastAPI()

class ProcesaPago(BaseModel):
    producto: str
    monto: float

@app.get("/procesa")
def procesa(producto: str, monto: float):
    id = str(uuid.uuid4())

    # Imprimir el UUID en los logs de la aplicación para que se vea con kubectl logs
    print(f"UUID Generado para producto {producto}: {id}")

    return {
        "producto": producto,
        "monto": monto,
        "uuid": id
    }
