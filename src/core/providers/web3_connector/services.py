import json
import ssl

import certifi
from web3 import AsyncWeb3, WebsocketProviderV2
from web3.exceptions import TransactionNotFound

from src.apps.etherium_transaction.schemas.transaction import PrepareTransaction
from src.apps.etherium_transaction.services.transaction import TransactionService
from src.core.database.postgresql.session import context_session
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
                            print(inst)
                except TransactionNotFound as e:
                    print(e)
                    print("ass log")
                except Exception as e:
                    await w3.eth.unsubscribe(subscription_id)
                    print(e)
                    print("ass log")

# class Web3Websocket:
#     def __init__(self):
#         self.ssl_context = ssl.create_default_context(cafile=certifi.where())
#         self.w3 = AsyncWeb3.persistent_websocket(
#             WebsocketProviderV2("wss://sepolia.infura.io/ws/v3/db6569d310fd4fa8bba12e620d286f7a",
#                                 websocket_kwargs={'ssl': self.ssl_context}))
#
#     async def __aenter__(self):
#         print("Mb log")
#         return self
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print(f"Exception: {exc_type}, {exc_val}")
#         return False
#
#     async def get_transaction_by_hash(self, tx_hash) -> dict:
#         tx_data = await self.w3.eth.get_transaction(transaction_hash=tx_hash)
#         return json.loads(self.w3.to_json(tx_data))
#
#     async def subscribe(self):
#         subscription_id = await self.w3.eth.subscribe(subscription_type="newPendingTransactions")
#         return subscription_id
#
#     async def unsubscribe(self, subscription_id):
#         await self.w3.eth.unsubscribe(subscription_id)
#
#     async def run(self):
#         async with context_session() as session:
#             tx_service = TransactionService(session=session)
#             print("x")
#             sub_id = await self.subscribe()
#             print(sub_id)
#             while True:
#                 try:
#                     print(123)
#                     async for response in self.w3.ws.process_subscriptions():
#                         print(1)
#                         if tx_hash := response.get("result"):
#                             tx_data = await self.get_transaction_by_hash(tx_hash)
#                             validate = PrepareTransaction(**tx_data)
#                             inst = await tx_service.create(validate.model_dump())
#                             print(inst)
#                 except Exception as e:
#                     print(e)
#                     print("ass log")
#                 finally:
#                     await self.unsubscribe(sub_id)
