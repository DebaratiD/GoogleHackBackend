import os
from fastapi import APIRouter, HTTPException
from app.models import NewsModel
from dotenv import load_dotenv, find_dotenv
import requests

isAvlb = load_dotenv(find_dotenv())

router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}}
)


def create_newsModel(i)->NewsModel:
    return NewsModel(
        title=i['title'],
        source=i['source']['name'],
        author=i['author'],
        description=i['description'],
        url=str(i['url']),
        content=i['content'],
        image = i['urlToImage']
    )

@router.get("/home")
async def getAllSources():
    if(os.getenv("newsToken"))==None or isAvlb==False:
        raise HTTPException(500,"News Token could not be loaded")
    response = requests.get(url=f'https://newsapi.org/v2/top-headlines/sources?apiKey={os.getenv("newsToken")}')
    data = response.json()
    return data['sources']

# Example query would be like: localhost:8000/news/news_query/?q=india
@router.get("/news_query/")
async def getQueryNews(q="", source="", page=1, pageSize=100):
    if(os.getenv("newsToken"))==None or isAvlb==False:
        raise HTTPException(500,"News Token could not be loaded")
    
    params=[]
    if len(source)!=0:
        params.append(f'sources={source}')
    if len(q)!=0:
        params.append(f'q={q}')
    params.append(f'page={page}')
    params.append(f'pageSize={pageSize}')
    params.append(f'apiKey={os.getenv("newsToken")}')

    params = '&'.join(params)

    response = requests.get(url=f'https://newsapi.org/v2/everything?language=en&{params}')
    data = response.json()
    data = [create_newsModel(i) for i in data['articles']]
    return data