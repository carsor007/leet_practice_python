
def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5, 1]
    num_of_coins = 0

    for coin in coins:
        num_of_coins += cents / coin
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

    def min_coins_dp(cents):
        num_of_coins = [0] * (len(cents) + 1)
        num_of_coins[0] = 0
        for i in range(1, len(cents))