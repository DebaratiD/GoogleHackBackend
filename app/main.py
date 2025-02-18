from fastapi import FastAPI, HTTPException
from .routes import newsapi, gemini
from fastapi.middleware.cors import CORSMiddleware  
# from pathlib import Path

# env_path = Path('.')/'.env'
#load_dotenv(dotenv_path=env_path)


app = FastAPI()
app.include_router(newsapi.router)
app.include_router(gemini.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"Hello world from fast API."}
