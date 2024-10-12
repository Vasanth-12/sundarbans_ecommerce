from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    emailid: str
    mobilenumber: str
    ordercounts: int
