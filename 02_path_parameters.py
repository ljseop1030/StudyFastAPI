from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id): # 파라미터 타입 없을 때
    return {"item_id": item_id} ## 이거 dictionary를 반환하는거임. 괄호 주의


@app.get("/items/{item_id}/typed")
def get_integer(item_id: int): # 파라미터 integer. 파이썬은 primitive를 쓰지 않음
    return {"item_id": item_id}

@app.get("/users/me") # 경로 고정
def get_me(): # 파라미터 없음
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def get_user(user_id: str): # 파라미터 string
    return {"user_id": user_id}
