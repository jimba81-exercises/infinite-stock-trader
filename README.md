# Infinite Stock Trader
Automatic Infinite Stock Trader using Dollar-Cost Averaging algorithm


# 1. Early Research

## 1.1. Setup Broker Platform
### References:
- https://app.alpaca.markets/

[Alpaca](https://app.alpaca.markets/) is selected for trading API provider.

### 1.1.1. Register Broker Service
1. Follow [How to use Postman for Alpaca APIs](https://alpaca.markets/learn/try-our-postman-workspace-for-alpaca-apis)
2. Register Broker team and acquire assets
3. Put assets params to `.env` file
    - Ensure the assets params are stored in secure location

### 1.1.2. Test with PostMan
>Reference: https://docs.alpaca.markets/docs/getting-started-with-broker-api
1. Launch `PostMan`
2. Fork `Broker API Collections` to workspace
3. Create environment and put environment params (e.g. HOST, api_key, api_secret)
4. Send Request (e.g. GET Assets)

### 1.1.3. Get Start with Trading APIs
>Refernce: https://docs.alpaca.markets/docs/paper-trading
1. Run following command for testing:
    ```sh
    $ curl -v https://paper-api.alpaca.markets/v2/account
    ## Expect 'Unauthorized Error'
    ```

<br>

# 2. Setup Project
## 2.1. Init Poetry Project
>Reference: https://python-poetry.org/docs/cli/
```sh
$ poetry --version ## Ensure poetry works and version is returned
$ cd ${WORKSPACE}
$ rm -rf ./venv # Ensure exsitng ./venv is clear
$ poetry init # Init Poetry project, set params (e.g. package name)

$ poetry run python main.py # Run app

$ poetry add <some dependency>
```

<br>