from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me") # 고정 경로. (중괄호 없음). 고정경로는 가변경로 위에.
def get_me(): # 파라미터 없음
    return {"user_id": "the current user"}

# @app.get의 {items_id}: defines parameters. url에서 저 위치의 값을 찾아냄. 중괄호!! 헷갈리면 안됨
# get_item의 items_id : captured value를 함수에 넣는 인자
## both names must be equal

@app.get("/items/{item_id}")
def get_item(item_id): # 파라미터 타입 없을 때. 가능은 하지만 현실에서 이러면 안됨
    return {"item_id": item_id} ## 이거 dictionary를 반환하는거임. 괄호 주의


@app.get("/items/{item_id}/typed")
def get_integer(item_id: int): # 파라미터 integer. 파이썬은 primitive를 쓰지 않음
    return {"item_id": item_id}

@app.get("/users/{user_id}")
def get_user(user_id: str): # 파라미터 string
    """for clear documentation"""
    return {"user_id": user_id}
