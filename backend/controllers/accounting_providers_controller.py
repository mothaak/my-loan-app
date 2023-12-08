from flask import Blueprint, jsonify, request, current_app
from backend.models.accounting_provider import AccountingProvider

accounting_providers_controller = Blueprint('accounting_providers_controller', __name__)

@accounting_providers_controller.route('/accounting_providers', methods=['GET'])
def get_accounting_providers():
    try:
        accounting_providers: list[str] = AccountingProvider.get_hardcoded_data()
        
        if not accounting_providers:
            return jsonify({"message": "No accounting providers found"}), 404

        return jsonify(accounting_providers), 200
    except Exception as execption:
        current_app.logger.error(f"Error fetching accounting providers: {execption}")
        return jsonify({"message": "Internal server error"}), 500
