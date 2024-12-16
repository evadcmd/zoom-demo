from fastapi import FastAPI

from zoom_demo.router import zoom_auth

api = FastAPI()

api.include_router(zoom_auth.router)
