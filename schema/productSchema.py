from pydantic import BaseModel

class Product(BaseModel):
    id: str
    productname: str
    price: float
    count: int