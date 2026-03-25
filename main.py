from fastapi import FastAPI
from routes import router

app = FastAPI(title="LinkedList API")
app.include_router(router)