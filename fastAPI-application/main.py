from contextlib import asynccontextmanager

from fastapi import FastAPI
from uvicorn import run

from app import main_router as api_router
from core.config import settings
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == '__main__':
    run("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)

