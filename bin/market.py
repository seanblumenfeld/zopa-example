from decimal import Decimal


class Lender:

    def __init__(self, lender, rate, available):
        self.lender = lender
        self.rate = Decimal(rate)
        self.available = int(available)


class Market:

    def __init__(self, market_info=[]):
        """A class to hold the  market information.

        Args:
            market_info: a list of dicts, where each dict contains the
                         description of a lender.
        """
        self.lenders = []
        for lender in market_info:
            self.add_lender(lender)

    def add_lender(self, lender):
        if isinstance(lender, Lender):
            self.lenders.append(lender)
        else:
            self.lenders.append(Lender(**lender))

    def available_lenders(self, loan_amount):
        lenders = [l for l in self.lenders if l.available >= loan_amount]
        if not lenders:
            raise ValueError(
                'No lenders in the market have available funds'
                ' to satisfy your requested loan {0}.'.format(loan_amount)
            )
        return lenders

    @property
    def number_of_lenders(self):
        return len(self.lenders)

    def __getitem__(self, lender_name):
        return [l for l in self.lenders if l.lender == lender_name][0]
