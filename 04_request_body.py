from fastapi import FastAPI
from pydantic import BaseModel # basemodel import

app = FastAPI()


# Basemodel은 validate, json 형변환, 구조설계가 자동
# json(텍스트 덩어리) 다룰 때 사용 - json 내용을 클래스에 넣어서 다루기 쉽게 만들어주는거
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
def create_item(item:Item):
    return item

@app.post("/items/{item_id}")
def func(item:Item):
    return {"item_id": item_id, **item.dict()}


# field validation
class Item2(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float = Field(..., gt=0)  # Greater than 0
    tax: float | None = Field(None, ge=0)  # Greater than or equal to 

# Field () 사용해서 조건을 알아서 validate 하게 설정 가능

# nested models
class Image(BaseModel):
    url: str
    name: str

class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    images: list[Image] | None = None # nested!


# model configuration
class Item4(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    class Config:
        # 입력 예시 제공
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }