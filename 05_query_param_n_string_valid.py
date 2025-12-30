from fastapi import FastAPI, Query # import Query
# Query는 한 값이 조건에 부합하는지 안 하는지를 입력 받자마자 validate 해주는 역할.
# 여러줄의 if문 안 해도 되고 바로 validate 해줌.

## 이름이 Query 이므로 query parameters (? 뒤 optional 정보들) 에게 사용!!

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
def items(q: str | None = Query(default=None, max_length=50)):
    results = []
    if q:
        results =  [item for item in fake_items_db if q.lower() in item["item_name"].lower()]
    else:
        results = fake_items_db
    return results

# q는 입력받은 값. get한 값이 valid 한지 query로 확인
# q가 valid 하다면? 목록에 있는지 확인 -> 있으면 목록에 있는 data 반환 / 없으면 빈 리스트
# q에 입력된게 없으면 그냥 목록 전체 data 반환


@app.get("/items/search/")
def items2(q: str = Query(min_length=3, max_length=50, description="Search query"), limit: int = Query(10, ge=1, le=100, description="Maximum number of items")):
    results = [item for item in fake_items_db if q.lower() in item["item_name"].lower()]
    return {"query": q, "limit": limit, "results": results[:limit]}
    # 슬라이싱 해서 맨 앞 limit 개수만큼 보여주겠다

"""
🎨 Query Parameter Features

Validation Constraints

min_length: Minimum string length
max_length: Maximum string length
regex: Regular expression pattern
ge: Greater than or equal (numbers)
le: Less than or equal (numbers)
gt: Greater than (numbers)
lt: Less than (numbers)

Metadata and Documentation

description: Parameter description in docs
deprecated: Mark parameter as deprecated
include_in_schema: Include/exclude from OpenAPI schema
example: Example value for documentation

"""
# example
@app.get("/items/")
def read_items( q: str | None = Query( default=None, title="Query string", description="Query string for the items to search in the database", min_length=3, max_length=50, example="laptop" ) ):
    return {"q": q}

####### 유의사항

# consistency: None도. constraint 없어도 맞춰주기
@app.get("/items/")
def read_items( q: str | None = Query(default=None), limit: int = Query(default=10) ):
    pass

# 