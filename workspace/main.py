import sys
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

# For GUI apps (PyQt, Tkinter, etc.)
class App:
    def __init__(self):
        pass
    
    def run(self):
        api_key = 'CKCWQMTREGA3WJF7225HNCS2P6'
        secret_key = '7dssGxumLDubdRr6Ymgi6pJkNVRPk2TZBqii1hXtUSkU'
        trading_client = TradingClient(api_key, secret_key)

        # Get our account information.
        account = trading_client.get_account()

        # Check if our account is restricted from trading.
        if account.trading_blocked:
            print('Account is currently restricted from trading.')

        # Check how much money we can use to open new positions.
        print('${} is available as buying power.'.format(account.buying_power))
        return self.app.exec()  # or sys.exit(app.exec())
    


# ==================================
if __name__ == '__main__':
    app = App()
    sys.exit(app.run())