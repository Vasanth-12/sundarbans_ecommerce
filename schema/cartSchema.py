from pydantic import BaseModel

class Cart(BaseModel):
    userid: str
    productList: list