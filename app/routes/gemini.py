import os
from fastapi import APIRouter
from app.models import Question
import google.generativeai as genai
from dotenv import load_dotenv
import json


GEMINI_KEY = os.getenv("GEMINI_KEY")
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

router = APIRouter(
       prefix="/qapi",
        tags=["qapi"],
        responses={404: {"description": "Not found"}}
)


@router.post("/")
def AskGemini(req:Question):
    if len(req.ques)=="":
        return {"message":"Please enter a question"}
    response = model.generate_content(req.ques)
    try:
         response.text
         return response.text
    except Exception as e:
         return {"error": f"Error: {type(e).__name__} - {str(e)}"}

@router.post("/getstory")
def getStory(req:Question):
    if len(req.ques)=="":
        return {"message":"No content found"}
    q = f"Given the following content, generate a summarised version in a max of 25 lines as you would explain to a {10} year old child. Do not add any bullet points, but no paragraph should have more than 2 lines. For any content that is unsafe to read for children, make it safe so that they can get an idea on what is the context: \n {req.ques}"
    response = model.generate_content(q)
    try:
         response.text
         return response.text
    except Exception as e:
         return {"error": f"Error: {type(e).__name__} - {str(e)}"}