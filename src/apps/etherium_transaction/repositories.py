from sqlalchemy import select, func, BigInteger
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.etherium_transaction.models import Transaction
from src.core.database.postgresql.mixins import RetrieveMixin, CreateMixin


class TransactionRepo(RetrieveMixin, CreateMixin):

    def __init__(self, session: AsyncSession):
        self.model = Transaction
        self.session = session

    async def retrieve_statistic(self):
        query = select(func.count(Transaction.id).label("transaction_count"),
                       func.cast(func.avg(Transaction.gas_price), BigInteger).label("average_gas_price"))
        res = await self.session.execute(query)
        return dict(res.mappings().first())
