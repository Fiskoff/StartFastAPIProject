from fastapi import FastAPI
from uvicorn import run

from app import main_router as api_router
from core.config import settings


main_app = FastAPI()
main_app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == '__main__':
    run("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)

