import os
from fastapi import APIRouter
from app.models import Question
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

googleKEY = "AIzaSyAFD_COHQDlvTsK5UBPKVDTFuS58Go_e3Q"

router = APIRouter(
       prefix="/qapi",
        tags=["qapi"],
        responses={404: {"description": "Not found"}}
)


@router.post("/")
def AskGemini(req:Question):
    genai.configure(api_key=googleKEY)
    model = genai.GenerativeModel('gemini-pro')
    if len(req.ques)=="":
        return {"message":"Please enter a question"}
    response = model.generate_content(req.ques)
    try:
         response.text
         return response.text
    except Exception as e:
         print(f'{type(e).__name__}: {e}')

@router.post("/getstory/")
def getStory(req:Question):
    genai.configure(api_key=googleKEY)
    model = genai.GenerativeModel('gemini-pro')
    if len(req.ques)=="":
        return {"message":"No content found"}
    q = f"Given the following content, generate a summarised version in a max of 25 lines as you would explain to a 10 year old child: \n {req.ques}"
    response = model.generate_content(q)
    try:
         response.text
         return response.text
    except Exception as e:
         print(f'{type(e).__name__}: {e}')