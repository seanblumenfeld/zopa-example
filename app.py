#! /usr/bin/env python
import csv
import sys

from bin import Calculator, Market


def _lowercase_file_headernames(file_data):
    return [{k.lower(): v for k, v in row.items()} for row in file_data]


def main(market_file, loan_amount):
    file_data = [r for r in csv.DictReader(market_file)]
    market_info = _lowercase_file_headernames(file_data)
    market = Market(market_info=market_info)
    calculator = Calculator(market=market)
    try:
        quote = calculator.get_quote(int(loan_amount))
    except ValueError as e:
        print('Loan not possible, reason: {}'.format(e))
    else:
        print('Requested amount: £{0}'.format(loan_amount))
        print('Rate: {0}'.format(quote.pretty_rate))
        print('Monthly repayment: £{0}'.format(quote.monthly_repayment))
        print('Total repayment: £{0}'.format(quote.total_repayment))
        return quote


if __name__ == "__main__":
    market_file = sys.argv[1]
    loan_amount = sys.argv[2]
    with open(market_file) as f:
        main(f, loan_amount)
