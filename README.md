# ETH Transaction Processor

The ETH Transaction microservice is a service developed using FastAPI that manages the processing of transactions on the Ethereum blockchain. This service offers features for retrieving, recording, and examining Ethereum transactions. It employs SQLAlchemy for database operations and Redis for caching solutions.

## Table of Contents

- [Introduce](#introduce)
- [Requirements](#requirements)
- [Installation](#installation)

## Introduce

- **Fetch Ethereum Transactions**: Retrieve Ethereum transactions from the blockchain using Infura.
- **Store Transactions in Database**: Save transactions in a PostgreSQL database for persistence and later analysis.
- **Analyze Transaction Data**: Perform analysis on stored transactions, such as calculating the average gas price.
- **Cache Results**: Use Redis to cache responses, reducing load times and improving performance.
- **Asynchronous Task Processing**: Utilize Celery for handling asynchronous tasks such as fetching and saving transactions.

## Requirements

- **Docker**: For containerization and environment consistency.
- **Docker Compose**: To manage multi-container Docker applications.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Kempasso/EtheriumStorage.git
cd EtheriumStorage
```

## 2. Create a .env File:

Env example contains testing credentials for `.env` file, however you need to write your Infura api token:

```bash
cp .envexample .env
```

```env
# POSTGRESQL CREDS
POSTGRES_USER='test'
POSTGRES_PASSWORD='1234pass'
POSTGRES_DB='test'
POSTGRES_PORT=5432
POSTGRES_HOST='postgres'

# REDIS
REDIS_PORT=6379
REDIS_HOST=redis

# INFURA
INFURA_API_TOKEN=<YOUR-API-TOKEN> # Need to be written
INFURA_WS_DOMAIN='wss://sepolia.infura.io/ws/v3/' # Test network
```

## 3.Start Docker Containers:


```bash
sudo docker compose up -d
```
Write the password.

