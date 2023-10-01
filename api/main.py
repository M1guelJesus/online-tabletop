from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.websockets import ws_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ws_router)


@app.get("/")
async def root():
    return RedirectResponse("/docs")
