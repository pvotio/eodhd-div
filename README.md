# EODHD Div
## Overview
EODHD Div is a Python-based data pipeline that retrieves dividend data for stocks using the EOD Historical Data API. The data is processed, transformed, and stored in a Microsoft SQL Server database.

## Features
- Fetches historical dividend data for multiple stock tickers.
- Implements a retry mechanism for reliable API requests.
- Utilizes multi-threading for efficient data retrieval.
- Stores processed data into a Microsoft SQL Server database.
- Supports logging and configurable settings via environment variables.
- Dockerized for easy deployment.

## Installation
### Prerequisites
- Python 3.10+
- Microsoft SQL Server
- Docker (optional, for containerized execution)

### Setup
Clone the repository:

```bash
git clone https://github.com/arqs-io/eodhd-div.git
cd eodhd-div
```

Install dependencies:

`pip install -r requirements.txt`

Set up environment variables:

- Copy .env.sample to .env
- Edit .env to include your database and API credentials.

Run the application:
`python main.py`

## Docker Usage

To run the application using Docker:


```bash
docker build -t eodhd-div .
docker run --env-file .env eodhd-div
```

## Contributing
- Fork the repository.
- Create a feature branch: git checkout -b feature-branch
- Commit changes: git commit -m "Add new feature"
- Push to the branch: git push origin feature-branch
- Open a Pull Request.