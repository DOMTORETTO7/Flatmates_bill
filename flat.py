class Bill:
    """
    object that contains data about the bill,
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Flatmate person who lives in the flat and
    pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, guest):
        weight = self.days_in_house / (self.days_in_house + guest.days_in_house)
        to_pay = bill.amount * weight
        return to_pay