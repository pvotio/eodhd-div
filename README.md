# EODHD Dividends Pipeline

This project automates the retrieval, transformation, and ingestion of **historical dividend data** from the [EOD Historical Data API](https://eodhistoricaldata.com/) for a universe of financial instruments. It supports multi-threaded execution for performance and loads structured dividend records into a Microsoft SQL Server database.

## Overview

### Purpose

The pipeline automates the following tasks:
- Fetches up to 5 years of dividend data for a list of tickers.
- Parses and enriches the dividend history using EODHD’s `/div/{ticker}` endpoint.
- Inserts cleaned and structured records into a database table.

It is designed for financial platforms and analysts needing a robust dividend history ingestion workflow.

## Source of Data

The data is obtained from the **EODHD Dividend Endpoint**:

- **Endpoint**: `/div/{ticker}`
- **Parameters**: `from=<date>` for lookback control
- **Output**: JSON records of dividend history

Authentication is token-based via a query string parameter.

## Application Flow

The workflow in `main.py` proceeds as follows:

1. **Load Tickers**:
   - Queries the DB to load tickers and maps them to Bloomberg-equivalent symbols.

2. **Initialize Engine**:
   - An `Engine` class handles threaded API calls to retrieve dividend data.

3. **Fetch Dividend Data**:
   - 10 threads concurrently query EODHD for 5-year histories per ticker.

4. **Transform & Load**:
   - Transformed data is structured via `transformer.Agent` and batch-inserted into SQL Server.

## Project Structure

```
eodhd-div-main/
├── client/                 # API and ETL engine logic
│   ├── engine.py           # Threaded data fetch manager
│   └── eodhd.py            # API wrapper for dividend endpoint
├── config/                 # Logger and settings config
├── database/               # SQL Server connection helpers
├── transformer/            # Data preparation logic
├── main.py                 # ETL runner
├── .env.sample             # Sample environment config
├── Dockerfile              # Docker containerization config
```

## Environment Variables

You must configure a `.env` file from the provided `.env.sample`. Important settings:

| Variable | Description |
|----------|-------------|
| `TOKEN` | EODHD API token |
| `OUTPUT_TABLE` | SQL Server table for dividend insert |
| `MSSQL_*` | SQL Server connection credentials |
| `INSERTER_MAX_RETRIES` | DB insert retry attempts |
| `REQUEST_MAX_RETRIES`, `REQUEST_BACKOFF_FACTOR` | Retry logic for API requests |

## Docker Support

You can run this ETL containerized:

### Build
```bash
docker build -t eodhd-dividends .
```

### Run
```bash
docker run --env-file .env eodhd-dividends
```

## Requirements

Install Python packages with:

```bash
pip install -r requirements.txt
```

Key packages:
- `requests`: API requests
- `pandas`: DataFrame handling
- `pyodbc`, `SQLAlchemy`: SQL Server integration
- `fast-to-sql`: Efficient database loading
- `python-decouple`: .env configuration support

## Running the Pipeline

Ensure that the `.env` file is configured. Then run:

```bash
python main.py
```

Output will log:
- Ticker load success
- Thread execution and API completion
- Number of dividend records inserted

## License

MIT License. Please ensure your EODHD API access adheres to licensing and fair use policies.