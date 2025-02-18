from pydantic import BaseModel

class NewsModel(BaseModel):
    title:str
    source:str
    author:str | None
    description:str | None
    url:str | None
    content:str
    image:str | None

class Question(BaseModel):
    ques:str