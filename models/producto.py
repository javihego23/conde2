from pydantic import BaseModel
from typing import Optional


class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    stock: int
