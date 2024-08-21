import json
import ssl

import certifi
from web3 import AsyncWeb3, WebsocketProviderV2
from web3.exceptions import TransactionNotFound

from src.apps.etherium_transaction.schemas import PrepareTransaction
from src.apps.etherium_transaction.services import TransactionService
from src.core.database.postgresql.session import context_session
from src.core.logger import tx_logger
from src.core.settings import config


async def upload_tx_websocket():
    url = f"{config.infura_settings.infura_ws_domain}{config.infura_settings.infura_api_token}"
    async with context_session() as session:
        tx_service = TransactionService(session=session)
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with AsyncWeb3.persistent_websocket(
                WebsocketProviderV2(url, websocket_kwargs={'ssl': ssl_context})) as w3:
            subscription_id = await w3.eth.subscribe(subscription_type="newPendingTransactions")
            while True:
                try:
                    async for response in w3.ws.process_subscriptions():
                        if tx_hash := response.get("result"):
                            tx_data = await w3.eth.get_transaction(transaction_hash=tx_hash)
                            prepared_tx = json.loads(w3.to_json(tx_data))
                            validate = PrepareTransaction(**prepared_tx)
                            inst = await tx_service.create(validate.model_dump())
                except TransactionNotFound as e:
                    tx_logger.error(e)
                except Exception as e:
                    await w3.eth.unsubscribe(subscription_id)
                    tx_logger.error(e)