from fastapi import FastAPI, HTTPException
from requester import requester
from requester.code_list_request_base_mode import CodeListRequest
from responser import responser

app = FastAPI()




@app.get("/")
async def home():
    return {"state": "working"}


@app.post("/insight")
async def insight(request: CodeListRequest):
    code_list = request.code_list

    code_files = []
    for code_item in code_list:
        if len(code_item) != 1:
            raise HTTPException(status_code=400, detail="Invalid code_list format")
        filename, content = next(iter(code_item.items()))
        code_file = {"filename": filename, "content": content}
        code_files.append(code_file)

    req = requester.OpenApiCodeInsightRequester(code_list=code_files)
    res = req.send_code_to_insight()

    json_response = responser.Responser(res).to_json()
    return json_response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000)
