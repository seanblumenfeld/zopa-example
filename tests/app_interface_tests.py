import io
from decimal import Decimal
import unittest

import app


class AppTests(unittest.TestCase):

    def test_main(self):
        market_file = io.StringIO('Lender,Rate,Available\nA,0.07,2000')
        quote = app.main(market_file, 1000)
        self.assertEquals(quote.loan_amount, 1000)
        self.assertEquals(quote.rate, Decimal('0.07'))
        self.assertEquals(quote.monthly_repayment, Decimal('30.88'))
        self.assertEquals(quote.total_repayment, Decimal('1111.68'))
