# Binance Futures Testnet Trading Bot

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- Input Validation
- Logging
- Error Handling
- Binance Futures Testnet

## Installation

```bash
git clone <repo_url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env:

```env
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

## Usage

### Market BUY

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

### Market SELL

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type MARKET \
--quantity 0.001
```

### Limit BUY

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--quantity 0.001 \
--price 90000
```

### Limit SELL

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 120000
```

## Logs

Logs are stored in:

```text
logs/trading_bot.log
```

## Assumptions

- User has a Binance Futures Testnet account.
- API credentials are valid.
- Symbol exists on Binance Futures Testnet.
