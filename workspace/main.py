import sys
from src.trader import Trader




#==============================
# CONSTANTS
ENV_FILE_PATH = '../docker-volumes/.env'


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
    app = App()
    sys.exit(app.run())