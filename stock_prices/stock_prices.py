#!/usr/bin/python

import argparse


def find_max_profit(prices):
    maxProfit = 0

    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if (i+1 < len(prices)):
                if (maxProfit == 0):
                    maxProfit = prices[j] - prices[i]
                if (maxProfit < prices[j] - prices[i]):
                    maxProfit = prices[j] - prices[i]

    return maxProfit


print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
