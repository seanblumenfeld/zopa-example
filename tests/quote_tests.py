from decimal import Decimal
import unittest

from bin import Calculator, Market, Lender


class BDDTests(unittest.TestCase):

    def _setup_market_1_calculator(self):
        lender_a = Lender('Lender A', '0.07', '10000')
        market = Market(market_info=[lender_a])
        return Calculator(market=market)

    def test_can_only_borrow_in_100_incriments(self):
        """Borrowers should be able to request a loan of any £100 increment
        between £1000 and £15000 inclusive.
        """
        calculator = self._setup_market_1_calculator()
        self.assertRaises(ValueError, calculator.get_quote, 1501)
        self.assertRaises(ValueError, calculator.get_quote, 1550)
        self.assertRaises(ValueError, calculator.get_quote, 0)

    def test_can_borrow_in_valid_range(self):
        """Borrowers should be able to request a loan of any £100 increment
        between £1000 and £15000 inclusive.
        """
        calculator = self._setup_market_1_calculator()
        quote = calculator.get_quote(loan_amount=1500)
        self.assertTrue(quote)

    def test_borrow_outside_valid_range_raises_error(self):
        """Borrowers should be able to request a loan of any £100 increment
        between £1000 and £15000 inclusive.
        """
        calculator = self._setup_market_1_calculator()
        self.assertRaises(ValueError, calculator.get_quote, loan_amount=999)
        self.assertRaises(ValueError, calculator.get_quote, loan_amount=15001)

    def test_no_sufficient_lenders_available_in_market(self):
        """If the market does not have sufficient offers from lenders to
        satisfy the loan then the system should inform the borrower that it
        is not possible to provide a quote at that time.
        """
        calculator = self._setup_market_1_calculator()
        self.assertRaises(ValueError,  calculator.get_quote, 11000)

    def test_borrow_1000_from_market_1(self):
        calculator = self._setup_market_1_calculator()
        quote = calculator.get_quote(loan_amount=1000)
        self.assertEquals(quote.loan_amount, 1000)
        self.assertEquals(quote.lender.rate, Decimal('0.07'))
        self.assertEquals(quote.monthly_repayment, Decimal('30.88'))
        self.assertEquals(quote.total_repayment, Decimal('1111.68'))

    def test_borrow_5100_from_market_1(self):
        calculator = self._setup_market_1_calculator()
        quote = calculator.get_quote(loan_amount=5100)
        self.assertEquals(quote.loan_amount, 5100)
        self.assertEquals(quote.lender.rate, Decimal('0.07'))
        self.assertEquals(quote.monthly_repayment, Decimal('157.48'))
        self.assertEquals(quote.total_repayment, Decimal('5669.28'))

    def _setup_market_2_calculator(self):
        lender_a = Lender('Lender A', '0.07', '1000')
        lender_b = Lender('Lender B', '0.1', '5000')
        lender_c = Lender('Lender C', '0.08', '10000')
        market_info = [lender_a, lender_b, lender_c]
        market = Market(market_info=market_info)
        return Calculator(market=market)

    def test_borrow_from_market_2_chooses_best_lender(self):
        calculator = self._setup_market_2_calculator()
        quote = calculator.get_quote(loan_amount=5100)
        self.assertEquals(quote.lender.lender, 'Lender C')


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
