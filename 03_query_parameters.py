# Query Parameters - Following the Official FastAPI Tutorial
# Learn how to handle optional parameters in URLs

# optional parts: 정렬(Sorting), 필터링(Filtering), 검색(Searching)

# https://example.com/items?skip=0&limit=10 <- ? 를 기준으로 나눔
# ? 앞은 path, ? 뒤는 query

# URL 경로에 없는 함수 파라미터는 전부 query parameter "q"


from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
# default value: optional이니까, 입력하지 않을 경우 skip 0, limit 10으로 진행.
## default value는 meaningful 해야함. 적당히 작거나 적당히 크게 금지.
def endpoint (skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}



@app.get("/items/{item_id}")
# q: str | None = None -> q는 str이거나 None. optional임.
## optional 일 때 None 처리 까먹으면 안됨
def mix (item_id, q: str | None = None): # 예제. 원래는 type hint 필요.
    return {"item_id": item_id, "q": q}

@app.get("/items/")
# 타입은 자동변환 됨.
# type hint로 자동 validation 이용하기.
def read_items(skip: int = 0, limit: int = 10, active: bool = True):
    return { "skip": skip, # Converted to int
    "limit": limit, # Converted to int
    "active": active # Converted to bool
    }

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, active: bool = True):
    # In a real app, you'd filter from a database
    return {
        "skip": skip,
        "limit": limit, 
        "active_only": active,
        "message": f"Showing {limit} users, skipping {skip}, active: {active}"
    }
