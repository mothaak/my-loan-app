from flask import Flask
from flask_cors import CORS
from backend.controllers.loan_application_controller import loan_application_controller
from backend.controllers.accounting_providers_controller import accounting_providers_controller

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(loan_application_controller, url_prefix='/api')
app.register_blueprint(accounting_providers_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3300, debug=True)
