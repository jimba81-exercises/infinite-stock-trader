# Infinite Stock Trader - Early Research

## Table of Contents
1. [Setup Trader Platform](#1-setup-trader-platform)

<br>

# 1. Setup Trader Platform - Alpaca
### References:
- https://app.alpaca.markets/

[Alpaca](https://app.alpaca.markets/) is selected for trading API provider.

## 1.1. Register Trader Service
1. Follow [How to use Postman for Alpaca APIs](https://alpaca.markets/learn/try-our-postman-workspace-for-alpaca-apis)
2. Register Broker team and acquire assets
3. Put assets params to `.env` file
    - Ensure the assets params are stored in secure location

## 1.2. Test with PostMan
>Reference: https://docs.alpaca.markets/docs/getting-started-with-broker-api
1. Launch `PostMan`
2. Fork `Broker API Collections` to workspace
3. Create environment and put environment params (e.g. HOST, api_key, api_secret)
4. Send Request (e.g. GET Assets)


<br>
