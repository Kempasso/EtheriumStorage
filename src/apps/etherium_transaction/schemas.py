from typing import Union, Optional

from pydantic import BaseModel, Field


class PrepareTransaction(BaseModel):
    hash: Union[str, None]
    from_address: Union[str, None] = Field(validation_alias="from")
    to_address: Union[str, None] = Field(validation_alias="to")
    value: int
    gas: int
    gas_price: int = Field(validation_alias="gasPrice")
    max_fee_per_gas: Union[int, None] = Field(validation_alias="maxFeePerGas", default=None)
    type: int
    nonce: int
    block_number: Union[int, None] = Field(validation_alias="blockNumber")
    input: str


class ReadTransaction(BaseModel):
    hash: Union[str, None]
    from_address: Union[str, None]
    to_address: Union[str, None]
    value: int
    gas: int
    gas_price: int
    max_fee_per_gas: Union[int, None]
    type: int
    nonce: int
    block_number: Union[int, None]
    input: str


class TxFilterParams(BaseModel):
    type: Optional[int] = None
    from_address: Optional[str] = None
    to_address: Optional[str] = None
    value: Optional[int] = None
    gas: Optional[int] = None
    gas_price: Optional[int] = None
    max_fee_per_gas: Optional[int] = None

    class Config:
        extra = "ignore"
