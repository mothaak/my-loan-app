import pytest
from services.balance_sheet_service import BalanceSheetService
from services.decision_engine import process_loan_application, calculate_pre_assessment
from unittest.mock import patch

sample_balance_sheet = [
    {"year": 2020, "month": 1, "profitOrLoss": 10000, "assetsValue": 50000},
    {"year": 2020, "month": 2, "profitOrLoss": -5000, "assetsValue": 40000},
]

@pytest.fixture
def mock_balance_sheet_service(monkeypatch):
    def mock_get_balance_sheet(accounting_provider_name):
        return sample_balance_sheet
    monkeypatch.setattr(BalanceSheetService, "get_balance_sheet", mock_get_balance_sheet)

def test_process_loan_application(mock_balance_sheet_service):
    result = process_loan_application("45000", "XERO")
    assert "preAssessmentResult" in result

def test_calculate_pre_assessment_profitable():
    pre_assessment = calculate_pre_assessment(sample_balance_sheet, "45000")
    assert pre_assessment == "60" 

def test_calculate_pre_assessment_high_assets():
    pre_assessment = calculate_pre_assessment(sample_balance_sheet, "30000")
    assert pre_assessment == "100"

def test_calculate_pre_assessment_default():
    adjusted_balance_sheet = [
        {"year": 2020, "month": 1, "profitOrLoss": -10000, "assetsValue": 30000},
        {"year": 2020, "month": 2, "profitOrLoss": -5000, "assetsValue": 20000},
    ]
    pre_assessment = calculate_pre_assessment(adjusted_balance_sheet, "100000")
    assert pre_assessment == "20"

