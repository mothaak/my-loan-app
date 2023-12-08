class BalanceSheetService:
    # In the real world this is where we would call accounting provider API
    @staticmethod
    def get_balance_sheet(accounting_provider_name) -> list[dict[str, int]]:
        hardcoded_balance_sheet: dict[str, list[dict[str, int]]] = {
            "XERO": [
                {"year": 2023, "month": 1, "profitOrLoss": 150000, "assetsValue": 20000},
                {"year": 2023, "month": 2, "profitOrLoss": -50000, "assetsValue": 15000},
                {"year": 2023, "month": 3, "profitOrLoss": 70000, "assetsValue": 18000},
                {"year": 2023, "month": 4, "profitOrLoss": 50000, "assetsValue": 21000},
                {"year": 2023, "month": 5, "profitOrLoss": 95000, "assetsValue": 23000},
                {"year": 2023, "month": 6, "profitOrLoss": -20000, "assetsValue": 12000},
                {"year": 2023, "month": 7, "profitOrLoss": 30000, "assetsValue": 19000},
                {"year": 2023, "month": 8, "profitOrLoss": 80000, "assetsValue": 22000},
                {"year": 2023, "month": 9, "profitOrLoss": -10000, "assetsValue": 14000},
                {"year": 2023, "month": 10, "profitOrLoss": 60000, "assetsValue": 25000},
                {"year": 2023, "month": 11, "profitOrLoss": -30000, "assetsValue": 16000},
                {"year": 2023, "month": 12, "profitOrLoss": 120000, "assetsValue": 25000}
            ],
            "MYOB": [
                {"year": 2023, "month": 1, "profitOrLoss": 100000, "assetsValue": 30000},
                {"year": 2023, "month": 2, "profitOrLoss": -20000, "assetsValue": 10000},
                {"year": 2023, "month": 3, "profitOrLoss": 50000, "assetsValue": 15000},
                {"year": 2023, "month": 4, "profitOrLoss": 20000, "assetsValue": 12000},
                {"year": 2023, "month": 5, "profitOrLoss": -15000, "assetsValue": 8000},
                {"year": 2023, "month": 6, "profitOrLoss": 45000, "assetsValue": 17000},
                {"year": 2023, "month": 7, "profitOrLoss": 30000, "assetsValue": 13000},
                {"year": 2023, "month": 8, "profitOrLoss": 70000, "assetsValue": 24000},
                {"year": 2023, "month": 9, "profitOrLoss": -25000, "assetsValue": 11000},
                {"year": 2023, "month": 10, "profitOrLoss": 55000, "assetsValue": 20000},
                {"year": 2023, "month": 11, "profitOrLoss": -35000, "assetsValue": 9000},
                {"year": 2023, "month": 12, "profitOrLoss": 90000, "assetsValue": 22000}
            ]
        }

        return hardcoded_balance_sheet.get(accounting_provider_name, [])