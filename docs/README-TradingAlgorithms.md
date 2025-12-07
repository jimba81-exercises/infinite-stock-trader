# Infinite Stock Trader - Trading Algorithms

## Table of Contents
1. [Overview](#1-overview)
2. [Glossary](#2-glossary)
3. [Algorithm - RaoR's Infinite Buying Strategy (무한매수법)](#2-algorithm---raors-infinite-buying-strategy-무한매수법)


<br>

# 1. Overview
The **Infinite Stock Trader** app supports user-defined trading algorithms that are described on this page. 

The app can automatically execute scheduled trades using the selected algorithms and the total allocated budget. Algorithm selection and configuration are defined in the `environment file`, which determines which strategies are active and how they are applied during scheduled trading cycles.

<br>

# 2. Glossary
- LOC: A Limit-On-Close (LOC) order is a type of order where you specify the maximum price you are willing to pay (for a buy) or the minimum price you are willing to accept (for a sell), but the order is executed only at the market close.

<br>

# 3. Algorithm - RaoR's Infinite Buying Strategy (무한매수법)

## References:
- https://namu.wiki/w/%EB%9D%BC%EC%98%A4%EC%96%B4%EC%9D%98%20%EB%AF%B8%EA%B5%AD%EC%A3%BC%EC%8B%9D%20%EB%AC%B4%ED%95%9C%EB%A7%A4%EC%88%98%EB%B2%95
- https://m.blog.naver.com/mortley/222577958223
- https://youtu.be/HrlY2AGaa8Q?si=sIsNyjrDFTykp2Ok

## 3.1. Abstraction
**RaoR’s Infinite Buying Strategy** is a systematic method of continuously buying a fixed amount of shares at regular intervals, regardless of market conditions, to steadily build a long-term position and take advantage of price fluctuations.

## 3.2. Parameters

| Parameter | Description | Type | Example (Default First) |
|-----------|-------------|------|---------|
| Initial Deposit | Total capital allocated for investment | Currency | $10,000, ... |
| Split | Number of equal parts to divide the initial deposit | Integer | 40, 20 |
| Interval | Time period between each purchase | Days | 1, 2 |
| Stock Code | Ticker symbol of the stock or ETF to purchase | Ticker Symbol | TQQQ, SOXL |
| Target Margin | Desired profit margin (% above average cost) at which to sell all shares | % | 10, 20

## 3.3. Algorithm
### 3.3.1. First Day Setup
1. Prepare `Initial Deposit` to the trading fund pool.
2. Set `Split`, `Interval`, evaluate `Single Trade Budget`
3. Select `Stock Code`
4. Buy Stock(s) with `Single Trade Budget` using a Limit-On-Close(LOC) order at any time of the day.

### 3.3.2. Trading
>**NOTE:** Trading occurs every `Interval`(days) at 10am (few moment after market open, LOC order is allowed)
1. If **All Stocks Sold**, execute `First Day Setup` and complete for the day.
2. Create **BUY** Order
    - Create only if current budget is greater than `Single Trade Budget`
    - Price: **Average Cost**
    - Type: LOC
    - Amount: `Single Trade Budget`
3. Create **SELL** Order
    - Price: **Average Cost** + (100 + `Target Margin`)%
    - Type: LOC
    - Amount: **ALL**

## Backtest
- Backtest is executed and result is shown in [here](./JyooBacktest20251206.pdf)
- The Infinite Buying Strategy is **NOT** really better off than conventional stratgies such as ``LSI`` or ``DCA``.



<br>



