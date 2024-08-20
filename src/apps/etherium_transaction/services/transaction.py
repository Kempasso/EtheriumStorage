from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.etherium_transaction.repository.transaction import TransactionRepo


class TransactionService:

    def __init__(self, session: AsyncSession):
        self.repository = TransactionRepo(session=session)

    async def get_first_values(self, **kwargs):
        instance = await self.repository.get_first_by_values(**kwargs)
        return instance

    async def get_many_by_values(self, offset, limit, **kwargs):
        return await self.repository.get_many_by_values(offset=offset, limit=limit, **kwargs)

    async def create(self, tx_data):
        instance = await self.repository.create(**tx_data)
        return instance

    async def retrieve_tx_statistic(self):
        return await self.repository.retrieve_statistic()
