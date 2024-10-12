from pydantic import BaseModel
from schema.userSchema import User

class Order(BaseModel):
    id: str
    user: dict
    productlist: list
    totalcost: float
    actualcost: float
    discountcost: float