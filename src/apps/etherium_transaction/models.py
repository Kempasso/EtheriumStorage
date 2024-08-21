from sqlalchemy import Column, Integer, String, Index, BigInteger
from src.core.database.postgresql.models import AbstractBase


class Transaction(AbstractBase):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, index=True, nullable=True)
    from_address = Column(String, index=True, nullable=True)
    to_address = Column(String, index=True, nullable=True)
    value = Column(BigInteger)
    gas = Column(Integer)
    gas_price = Column(BigInteger)
    max_fee_per_gas = Column(BigInteger, nullable=True)
    type = Column(Integer)
    nonce = Column(Integer)
    block_number = Column(Integer, index=True, nullable=True)
    input = Column(String)

    __table_args__ = (
        Index('ix_transactions_hash', 'hash'),
        Index('ix_transactions_from_address', 'from_address'),
        Index('ix_transactions_to_address', 'to_address'),
        Index('ix_transactions_block_number', 'block_number'),
    )
