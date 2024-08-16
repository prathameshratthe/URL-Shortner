from pydantic import BaseModel

class URLBase(BaseModel):
    long_url: str

class URLCreate(URLBase):
    short_code: str

class URL(URLBase):
    id: int
    short_code: str

    class Config:
        orm_mode = True
