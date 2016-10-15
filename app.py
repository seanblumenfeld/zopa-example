#! /usr/bin/env python

import sys


if __name__ == "__main__":
    market_file = sys.argv[1]
    loan_amount = sys.argv[2]
    print('{} : {}'.format(market_file, loan_amount))
