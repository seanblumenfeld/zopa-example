import unittest

from bin import Market, Lender


class LenderTests(unittest.TestCase):

    def test_lender_has_a_name(self):
        lender = Lender('L1', rate=0.1, available=100)
        self.assertEquals(lender.lender, 'L1')

    def test_lender_has_a_rate(self):
        lender = Lender('L1', rate=0.1, available=100)
        self.assertEquals(lender.rate, 0.1)

    def test_lender_has_available(self):
        lender = Lender('L1', rate=0.1, available=100)
        self.assertEquals(lender.available, 100)


class MarketTests(unittest.TestCase):

    def setUp(self):
        self.lender_a = Lender('Lender A', '0.1', '1000')
        self.lender_b = Lender('Lender B', '0.1', '2000')
        self.lender_c = Lender('Lender C', '0.1', '3000')

    def test_market_lenders_are_stored(self):
        market_info = [self.lender_a, self.lender_b, self.lender_c]
        market = Market(market_info=market_info)
        self.assertEquals(len(market.lenders), len(market_info))
        self.assertEquals(market_info, market.lenders)
        self.assertEquals(self.lender_a, market['Lender A'])

    def test_available_lenders_raises_when_no_lenders_in_market(self):
        market = Market()
        self.assertEquals(market.number_of_lenders, 0)
        self.assertRaises(ValueError, market.available_lenders, 1000)

    def test_available_lenders_raises_when_no_available_loan_amount(self):
        market = Market(market_info=[self.lender_a])
        self.assertRaises(ValueError, market.available_lenders, 2000)

    def test_available_lenders_returns_all_available_loaners(self):
        market_info = [self.lender_a, self.lender_b, self.lender_c]
        market = Market(market_info=market_info)
        lenders = market.available_lenders(loan_amount=2000)
        self.assertEquals(len(lenders), 2)
        self.assertIn(self.lender_b, lenders)
        self.assertIn(self.lender_c, lenders)
