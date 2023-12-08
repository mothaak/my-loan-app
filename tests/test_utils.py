import pytest
from backend.utils.exceptions import ApplicationException
from backend.utils.validation import validate_loan_application  

def test_validate_loan_application_valid():
    try:
        validate_loan_application("Test Business", "2010", "50000", "XERO")
    except ApplicationException:
        pytest.fail("Unexpected ApplicationException raised")

def test_validate_loan_application_no_business_name():
    with pytest.raises(ApplicationException) as excinfo:
        validate_loan_application("", "2010", "50000", "XERO")
    assert "Business name is required" in str(excinfo.value)

def test_validate_loan_application_no_year_established():
    with pytest.raises(ApplicationException) as excinfo:
        validate_loan_application("Test Business", "", "50000", "XERO")
    assert "Year established is required" in str(excinfo.value)

def test_validate_loan_application_no_loan_amount():
    with pytest.raises(ApplicationException) as excinfo:
        validate_loan_application("Test Business", "2010", "", "XERO")
    assert "Loan amount is required" in str(excinfo.value)

def test_validate_loan_application_no_accounting_provider_name():
    with pytest.raises(ApplicationException) as excinfo:
        validate_loan_application("Test Business", "2010", "50000", "")
    assert "Accounting provider is required" in str(excinfo.value)
