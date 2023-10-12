from fastapi import FastAPI
from models.producto import Producto

app = FastAPI()

productos = [
    {
        "id": 1,
        "nombre": "Producto 1",
        "precio": 20,
        "stock": 10
    },
{
        "id": 2,
        "nombre": "Producto 2",
        "precio": 30,
        "stock": 5
    }
]


@app.get('/')
def message():
    return "Hello Word !!!"


@app.get('/productos')
def get_productos():
    return productos


@app.get('/productos/{id}')
def get_producto(id: int):
    return list(filter(lambda item: item["id"] == id, productos))

#productos/?stock=10&precio=20 parametro Query
@app.get('/productos/')
def get_productos_by_stock(stock: int, precio: float):
    return list(filter(lambda item: item["stock"] == stock and item["precio"] == precio, productos))


@app.post('/productos')
def crear_producto(producto: Producto):
    productos.append(producto)
    return productos


@app.post('/productos')
def crear_producto(producto: Producto):
    productos.append(producto)
    return productos