import sys
from pathlib import Path
from src.trader import Trader
import toml


#==============================
# CONSTANTS

# Get the directory where main.py is located
MAIN_DIR = Path(__file__).parent

# Read version from pyproject.toml
with open(MAIN_DIR / 'pyproject.toml', 'r') as f:
    pyproject_data = toml.load(f)
VERSION = pyproject_data['project']['version']
APP_NAME = 'InfiniteStockTrader'
ENV_FILE_PATH = MAIN_DIR.parent / 'docker-volumes' / '.env'


#==============================
# APP
class App:
    def __init__(self):
        self.trader = Trader(ENV_FILE_PATH)
        self.trader.connect()
    
    def run(self):
        # Main application logic here
        pass
    


# ==================================
if __name__ == '__main__':
    print(f"\nStarting application: {APP_NAME} v{VERSION}...")
    app = App()
    print(f"\nApplication Exited\n")
    sys.exit(app.run())
    