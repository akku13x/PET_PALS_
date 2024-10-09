from donation import Donation

class ItemDonation(Donation):
    def __init__(self, donor_name: str, amount: float, item_type: str):
        super().__init__(donor_name, amount)
        self.item_type = item_type

    def record_donation(self):
        return f"Recorded item donation of {self.item_type} valued at ${self.amount} by {self.donor_name}"