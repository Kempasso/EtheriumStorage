## 1. List Transactions

**Endpoint:**

**http://localhost:8000/transaction/?offset=1&limit=10**

**Method**: GET

**Description**: Retrieve a list of transactions, with optional filtering by fields.

**Query Parameters**:

- `offset` (int): Number of page.
- `limit` (int): Maximum number of records to return.
-

**Response**:

- `200 OK`: A list of transactions.

**Example Response**:

```json
[
  {
    "hash": "0x6b69b89fdbe4...",
    "from_address": "0xD556A69614C...",
    "to_address": "0x5f54a69EF8099...",
    "value": 0,
    "gas": 119280,
    "gas_price": 120566061666,
    "max_fee_per_gas": 120566061666,
    "type": 2,
    "nonce": 16870,
    "block_number": null,
    "input": "0x00747d2415d78..."
  }
]
```

**Curl Command**:

```bash
curl -X GET "http://localhost:8000/transaction/?offset=1&limit=10" -H "accept: application/json"
```

## 2. Get Transaction by Hash

**Endpoint:**

**http://localhost:8000/transaction/{transaction_hash}**

**Method**: GET

**Description**: Retrieve transaction by hash.

**Path Parameter**:

- `tx_hash` (str): The hash of the transaction to retrieve.

**Response**:

- `200 OK`: Transaction data.
-

**Example Response**:

```json
{
  "hash": "0x6b69b89fdbe4...",
  "from_address": "0xD556A69614C...",
  "to_address": "0x5f54a69EF8099...",
  "value": 0,
  "gas": 119280,
  "gas_price": 120566061666,
  "max_fee_per_gas": 120566061666,
  "type": 2,
  "nonce": 16870,
  "block_number": null,
  "input": "0x00747d2415d78..."
}
```

**Curl Command**:

```bash
curl -X GET "http://localhost:8000/transaction/{transaction_hash}" -H "accept: application/json"
```

**Description:**

Websocket connection for getting statistic in realtime.

**Endpoint**:

ws://127.0.0.1:8000/transaction/statistic

**Description**: Retrieve statistics for the transactions.

**Every second data**:

```json
{
  "transaction_count": 40,
  "average_gas_price": 148805482604
}
```