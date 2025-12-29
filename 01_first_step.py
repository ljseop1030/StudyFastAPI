from fastapi import FastAPI # import

app = FastAPI() # create instance


# path operation

@app.get("/") # 여기로 들어오면
# / : path
# .get : HTTP method

## GET: read / POST: create / PUT: update / DELETE: delete

async def root(): # 이걸 실행시켜라
    return {"message": "Hello World"}