from fastapi import FastAPI


app = FastAPI()


@app.get("/t")
def get():
    return {"kk": "ffffffffffffffff"}