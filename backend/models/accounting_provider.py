class AccountingProvider:
    # Since we would have more providers in future, we will have a model for them 
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_hardcoded_data(cls):
        return ["XERO", "MYOB"]
