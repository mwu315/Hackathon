def maxProfit(prices):
    if len(prices) == 0:
        return 0
    curr_low = prices[0]
    max_profit = 0
    for price in prices:
        if price > curr_low:
            curr_low = price
            max_profit = max(max_profit, price - curr_low)
        return max_profit


