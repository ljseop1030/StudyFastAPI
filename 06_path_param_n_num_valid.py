from fastapi import FastAPI, Path, Query
# 사실상 query 사용법이랑 거의 동일. 그냥 사용 대상만 안 헷갈리면 될 듯.

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/{item_id}")
def item (item_id: int = Path(ge=1)):
    return{"item_id": item_id}

@app.get("/items/{item_id}/details")
def item2 (item_id: int = Path(ge=1, le=1000, description = "The ID of the item"), q: str | None = Query(default=None, max_length=50)):
    return {"item_id": item_id, "q": q, "details": "Item details here"}

@app.get("/users/{user_id}")
def item3 (user_id: int = Path(title="User ID", description="The ID of the user to get", ge=1)):
    return {"user_id": user_id, "message": f"User {user_id} profile"}