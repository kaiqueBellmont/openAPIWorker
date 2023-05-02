from fastapi import FastAPI

from requester import requester
from responser import responser

app = FastAPI()


@app.get("/")
async def home():
    return {"state": "working"}


@app.post("/insight")
async def insight(code_list: dict) -> dict:
    """
    :param code_list:
    :return:
    """
    if not isinstance(code_list, dict):
        raise TypeError

    req = requester.OpenApiCodeInsightRequester(code_list=code_list["code_list"])
    res = req.send_code_to_insight()

    json_response = responser.Responser(res).to_json()
    return json_response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000)
