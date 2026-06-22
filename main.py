from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def root():
    return {"message": "DecodeLabs P1 API is live ✓"}

products = [
    {"id": 1, "name": "Laptop",   "price": 75000},
    {"id": 2, "name": "Mouse",    "price": 499},
    {"id": 3, "name": "Keyboard", "price": 1200},
]
class Product(BaseModel):
    name: str
    price: float
@app.get("/products", status_code=200)
def get_all_products():
    return {
        "status": "ok",
        "count": len(products),
        "data": products
    }

@app.get("/products/{product_id}", status_code=200)
def get_product(product_id: int):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return {"status": "ok", "data": product}


@app.post("/products", status_code=201)
def create_product(product: Product):
    if not product.name.strip():
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty"
        )
    new = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }
    products.append(new)
    return {"status": "created", "data": new}

