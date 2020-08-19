##apibacktest

import alpaca_trade_api as tradeapi

API_KEY = ""#Add Your Key
API_SECRET = ""#Add your Secret Key
APCA_TRADE_API_BASE_URL = "https://paper-api.alpaca.markets"##Change to https://data.alpaca.markets/v2 for live market
APCA_DATA_API_BASE_URL = "https://data.alpaca.markets/v1"

tradeAPI = tradeapi.REST(API_KEY,API_SECRET,APCA_TRADE_API_BASE_URL)

# Check if the market is open now.
clock = tradeAPI.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Get our account information.
account = tradeAPI.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

# Get daily price data for AAPL over the last 5 trading days.
barset = tradeAPI.get_barset('AAPL', 'day', limit=5)
aapl_bars = barset['AAPL']

# Buy a position and add a stop-loss and a take-profit of 5 %
symbol = 'AAPL'
symbol_bars = tradeAPI.get_barset(symbol, 'minute', 1).df.iloc[0]
symbol_price = symbol_bars[symbol]['close']
tradeAPI.submit_order(
    symbol=symbol,
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc',
    order_class='bracket',
    stop_loss={'stop_price': symbol_price * 0.99,},
    take_profit={'limit_price': symbol_price * 1.01}
)



