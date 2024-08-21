import asyncio
from typing import Optional

from fastapi import APIRouter, Depends, WebSocketDisconnect, WebSocket, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.etherium_transaction.schemas import ReadTransaction, TxFilterParams
from src.apps.etherium_transaction.services import TransactionService
from src.core.database.postgresql.session import get_session
from fastapi_cache.decorator import cache

from src.core.logger import tx_logger

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])


@transaction_router.get("/", response_model=list[ReadTransaction])
@cache(expire=60)
async def get_filtered_transactions(params: TxFilterParams = Depends(), offset: Optional[int] = Query(1, gt=0),
                                    limit: Optional[int] = Query(10, gt=0),
                                    session: AsyncSession = Depends(get_session)):
    tx_service = TransactionService(session=session)
    filter_data = params.model_dump(exclude_unset=True, exclude_none=True)
    instances = await tx_service.get_many_by_values(offset=offset, limit=limit, **filter_data)
    return instances


@transaction_router.get("/{transaction_hash}", response_model=ReadTransaction)
async def get_transaction(transaction_hash: str, session: AsyncSession = Depends(get_session)):
    tx_service = TransactionService(session=session)
    return await tx_service.get_first_values(hash=transaction_hash)


@transaction_router.websocket("/statistic")
async def websocket_statistic(websocket: WebSocket, session: AsyncSession = Depends(get_session)):
    await websocket.accept()
    tx_service = TransactionService(session=session)
    try:
        while True:
            stat = await tx_service.retrieve_tx_statistic()
            await websocket.send_json(stat)
            await asyncio.sleep(1)
    except WebSocketDisconnect as e:
        tx_logger.info("WebSocket disconnect")
    except Exception as e:
        tx_logger.error(e)
    finally:
        tx_logger.info("WebSocket connection close")
        await websocket.close()