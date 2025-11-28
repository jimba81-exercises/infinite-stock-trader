import datetime
from dotenv import load_dotenv
import os

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

class Trader:
  def __init__(self, env_path: str):
    # TODO: Get from ENV not from file. This is to run from cloud server.
    """
    load_dotenv(env_path)
    self.__paper_mode = os.getenv('ALPACA_PAPER_MODE', 'True').strip() == 'True'
    self.__api_key = os.getenv('ALPACA_API_KEY')
    self.__secret_key = os.getenv('ALPACA_API_SECRET')
    self.__trading_client = None
    """
    
  def connect(self):
    # TODO: Implement with ENV
    return
    self.__trading_client = TradingClient(
        self.__api_key, 
        self.__secret_key,
        paper=self.__paper_mode
    )

    account = self.__trading_client.get_account()
    
    print(f"---------------------------------")
    print(f"Welcome {account.account_number}!")
    print(f" Current Time  : {datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z%z')}") 
    print(f" Account Type  : {'PAPER' if self.__paper_mode else 'LIVE'}")
    print(f" Status        : {account.status}")
    print(f" BuyingPower   : ${account.buying_power}")
    print(f" Trading State : {'BLOCKED' if account.trading_blocked else 'READY'}")
    print(f"")


    """ 
# Create LOC (Limit On Close) order
order = OrderRequest(
    symbol="AAPL",           # Stock symbol
    qty=10,                  # Number of shares
    side=OrderSide.BUY,      # BUY or SELL
    type=OrderType.LIMIT,    # Limit order
    time_in_force=TimeInForce.CLS,  # LOC order
    limit_price=170.50       # Limit price to buy at market close
)    
    """
    