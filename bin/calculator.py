class Calculator:

    def __init__(self, market):
        self.market = market
        self._loan_minimum = 1000
        self._loan_maximum = 15000

    def _is_valid_loan_request(self, loan_amount):
        """Check a loan amount request is valid.

        A valid loan is defined as:
            - Within the minimum and maximmum boundaries; set by market.
            - Is in an incriment of £100.
        """
        if not self._loan_minimum <= loan_amount <= self._loan_maximum:
            raise ValueError('loan_amount out of range.')
        if not loan_amount % 100 == 0:
            raise ValueError('loan_amount not valid.')

    def get_quote(self, loan_amount):
        """Calculate a Quote for a loan based on current market."""
        self._is_valid_loan_request(loan_amount)
        lenders = self.market.available_lenders(loan_amount)
        best_lender = min(lenders, key=lambda l: l.rate)
        return Quote(loan_amount, best_lender)


class Quote:

    def __init__(self, loan_amount, lender):
        self.loan_amount = loan_amount
        self.lender = lender
        self._rate_per_month = self.lender.rate/12
        self._loan_months = 36

    @property
    def monthly_repayment(self):
        m = self._rate_per_month + (self._rate_per_month / (1-(1+self._rate_per_month)**-self._loan_months)) * self.loan_amount  # noqa
        return round(m, 2)

    @property
    def total_repayment(self):
        return self.monthly_repayment * self._loan_months
