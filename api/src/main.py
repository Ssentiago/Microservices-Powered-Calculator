import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from views import views_router




app = FastAPI()
app.include_router(views_router)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

if __name__ == "__main__":
    print("API is running at http://127.0.0.1:8000/")
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
