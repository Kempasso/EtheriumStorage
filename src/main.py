import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, BackgroundTasks
from fastapi_cache.backends.redis import RedisBackend

from src.apps.etherium_transaction.routers.transaction import transaction_router
from src.core.providers.web3_connector.services import upload_tx_websocket
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from src.core.settings import config


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis = aioredis.from_url(config.redis_settings.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    asyncio.create_task(upload_tx_websocket())
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(transaction_router)

# @app.on_event("startup")
# async def startup():
#     asyncio.create_task(get_info())
