from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# import unicorn
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
def index(request: Request):
    """
    index
    """
    return templates.TemplateResponse(
        name="index.html",
        context={
            "name": "Vlad"
        },
        request=request)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,
            "q": q}
