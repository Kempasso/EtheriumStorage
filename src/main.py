import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache.backends.redis import RedisBackend

from src.apps.etherium_transaction.routers import transaction_router
from src.core.providers.web3_connector.services import upload_tx_websocket
from fastapi_cache import FastAPICache
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