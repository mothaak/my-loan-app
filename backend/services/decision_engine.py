from backend.services.balance_sheet_service import BalanceSheetService

def process_loan_application(loan_amount, accounting_provider_name) -> dict[str, str]:
    
    balance_sheet: list[dict[str, int]] = BalanceSheetService.get_balance_sheet(accounting_provider_name)

    pre_assessment_result: ['60', '100', '20'] = calculate_pre_assessment(balance_sheet, loan_amount)
    return {"preAssessmentResult": pre_assessment_result}

def calculate_pre_assessment(balance_sheet, loan_amount) -> ['60', '100', '20']:
    total_profit: int = sum(item['profitOrLoss'] for item in balance_sheet if item['profitOrLoss'] > 0)
    average_assets: float = sum(item['assetsValue'] for item in balance_sheet) / len(balance_sheet)
    loan_amount = int(loan_amount)

    if total_profit > 0 and average_assets <= loan_amount:
        pre_assessment = "60"
    elif average_assets > loan_amount:
        pre_assessment = "100"
    else:
        pre_assessment = "20"

    return pre_assessment
