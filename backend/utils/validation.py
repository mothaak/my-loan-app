from backend.utils.exceptions import ApplicationException

def validate_loan_application(business_name, year_established, loan_amount, accounting_provider_name) -> None:
    if not business_name:
        raise ApplicationException("Business name is required")
    if not year_established:
        raise ApplicationException("Year established is required")
    if not loan_amount:
        raise ApplicationException("Loan amount is required")
    if not accounting_provider_name:
        raise ApplicationException("Accounting provider is required")

