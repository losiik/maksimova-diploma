from fastapi import FastAPI

from .controllers.comments_controller import  comments_router


app = FastAPI(openapi_prefix="/api/v1")
app.include_router(comments_router)