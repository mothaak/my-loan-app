from flask import Blueprint, request, jsonify, current_app
from backend.services.balance_sheet_service import BalanceSheetService
from backend.services.decision_engine import process_loan_application
from backend.utils.exceptions import ApplicationException
from backend.utils.validation import validate_loan_application

loan_application_controller = Blueprint('loan_application_controller', __name__)

@loan_application_controller.route('/loan_application', methods=['POST'])
def loan_application():
    try:
        data = request.get_json()
        if not data:
            raise ApplicationException("No data provided")

        business_name: str = data.get('businessName')
        year_established: str = data.get('yearEstablished')
        loan_amount: str = data.get('loanAmount')
        accounting_provider_name: str = data.get('accountingProviderName')

        validate_loan_application(
            business_name=business_name,
            year_established=year_established,
            loan_amount=loan_amount,
            accounting_provider_name=accounting_provider_name
        )

        pre_assesmnent_result: dict[str, str] = process_loan_application(
            loan_amount=loan_amount,
            accounting_provider_name=accounting_provider_name
        )

        current_app.logger.info("Loan application processed successfully.")
        return jsonify(pre_assesmnent_result), 200
    except ApplicationException as e:
        current_app.logger.error(f"Application error: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


@loan_application_controller.route('/balance_sheet', methods=['GET'])
def balance_sheet():
    try:
        accounting_provider_name: str | None = request.args.get(key='accounting_provider_name')
        if not accounting_provider_name:
            raise ApplicationException(
                "accounting_provider_name parameter is missing")

        balance_sheet: list[dict[str, int]] = BalanceSheetService.get_balance_sheet(accounting_provider_name)
        current_app.logger.info(msg="Balance sheet fetched successfully.")
        return jsonify(balance_sheet), 200
    except ApplicationException as e:
        current_app.logger.error(msg=f"Application error: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(msg=f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500
